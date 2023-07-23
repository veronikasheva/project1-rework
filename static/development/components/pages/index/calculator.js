import "./calculator.scss";
import validation from "../../module/validation";

const tableDutyBasisAccrual = document.querySelector(
  ".calculator_result__table-duty-basis-accrual"
);
const tableDutyResult = document.querySelector(
  ".calculator_result__table-duty-result"
);
const tableExciseAccrual = document.querySelector(
  ".calculator_result__table-excise-basis-accrual"
);
const tableExciseRate = document.querySelector(
  ".calculator_result__table-excise-rate"
);
const tableExciseResult = document.querySelector(
  ".calculator_result__table-excise-result"
);
const tableVatBasisAccrual = document.querySelector(
  ".calculator_result__table-vat-basis-accrual"
);
const tableVatResult = document.querySelector(
  ".calculator_result__table-vat-result"
);

const calculator_btn = document.querySelector(".calculator__btn > button");
const category = document.querySelector('select[name="category"]');
let category_value = document.querySelector('select[name="category"]').value;

calculator_btn.addEventListener("click", calculate);

category.addEventListener("change", () => {
  category_value = document.querySelector('select[name="category"]').value;

  if (category_value === "trucks") {
    document.querySelector("#trucks-year").classList.remove("disabled");
    document.querySelector("#passenger-year").classList.add("disabled");
  } else {
    document.querySelector("#passenger-year").classList.remove("disabled");
    document.querySelector("#trucks-year").classList.add("disabled");
  }
});

function calculate(e) {
  e.preventDefault();
  const status = validation(calculator_btn);
  const current_year = new Date().getFullYear();

  const excise = ({ engine, year, fuel }) => {
    if (fuel.value === "hybrid") {
      return 100;
    }

    const cff_engine = engine / 1000;
    const cff_year =
      current_year - year > 15
        ? 15
        : current_year === year
        ? 1
        : current_year - year - 1;

    const rate =
      engine >= +fuel.dataset.lim
        ? +fuel.dataset.max_rate
        : +fuel.dataset.min_rate;

    tableExciseRate.textContent = `${cff_year}x${rate}`;

    return rate * cff_engine * cff_year;
  };

  const excise_trucks = ({ engine, year }) => {
    const cff =
      year === "-5" ? 0.02 : year === "5-8" ? 0.8 : year === "8+" ? 1 : 0.01;

    tableExciseRate.textContent = cff;

    return engine * cff;
  };

  if (status) {
    const price = +document.querySelector('input[name="price"]').value;
    const currency = +document.querySelector('input[name="currency"]:checked')
      .dataset.value;
    const engine = +document.querySelector('input[name="engine"]').value;
    const passengerYear = +document.querySelector(
      'select[name="passenger-year"]'
    ).value;
    const trucksYear = document.querySelector(
      'select[name="trucks-year"]'
    ).value;

    const fuel_select = document.querySelector('select[name="fuel"]');
    const fuel_selected_index = fuel_select.selectedIndex;
    const fuel = fuel_select.querySelectorAll("option")[fuel_selected_index];

    const excise_result =
      category_value === "trucks"
        ? excise_trucks({ engine, year: trucksYear })
        : excise({ engine, year: passengerYear, fuel });

    const cost = price / currency;
    const toll = cost * 0.1;
    const costWithDutyAndExcise = cost + excise_result + toll;
    const pdv = costWithDutyAndExcise * 0.2;

    const result = excise_result + toll + pdv;
    const result_currency_all = document.querySelectorAll(".result_currency");
    const result_currency_uan =
      +document.getElementById("result_uan").dataset.value;

    result_currency_all.forEach((result_currency) => {
      result_currency.innerHTML = Math.round(
        result * result_currency.dataset.value
      );
    });

    const getValueInUan = (value) =>
      `${Math.round(value * result_currency_uan)} ₴`;

    tableDutyBasisAccrual.textContent = getValueInUan(cost);
    tableDutyResult.textContent = getValueInUan(toll);
    tableExciseAccrual.textContent = `${engine} куб.см.`;
    tableExciseResult.textContent = getValueInUan(excise_result);
    tableVatBasisAccrual.textContent = getValueInUan(costWithDutyAndExcise);
    tableVatResult.textContent = getValueInUan(pdv);
  }
}
