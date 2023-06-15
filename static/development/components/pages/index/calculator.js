import "./calculator.scss";
import validation from "../../module/validation";

const calculator_btn = document.querySelector(".calculator__btn > button");
const category = document.querySelector('select[name="category"]');
let category_value = document.querySelector('select[name="category"]').value;

calculator_btn.addEventListener("click", calculate);

category.addEventListener("change", () => {
  category_value = document.querySelector('select[name="category"]').value;
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

    return rate * cff_engine * cff_year;
  };

  const excise_trucks = ({ engine, year }) => {
    const year_count = current_year - year;
    const cff =
      year_count === 0
        ? 0.01
        : year_count < 5
        ? 0.02
        : year_count < 8
        ? 0.8
        : 1;
    return engine * cff;
  };

  if (status) {
    const price = +document.querySelector('input[name="price"]').value;
    const currency = +document.querySelector('input[name="currency"]:checked')
      .dataset.value;
    const engine = +document.querySelector('input[name="engine"]').value;
    const year = +document.querySelector('select[name="year"]').value;

    const fuel_select = document.querySelector('select[name="fuel"]');
    const fuel_selected_index = fuel_select.selectedIndex;
    const fuel = fuel_select.querySelectorAll("option")[fuel_selected_index];

    const excise_result =
      category_value === "trucks"
        ? excise_trucks({ engine, year })
        : excise({ engine, year, fuel });

    const toll = (price / currency) * 0.1;
    const pdv = (price / currency + excise_result + toll) * 0.2;

    const result = excise_result + toll + pdv;
    const result_currency_all = document.querySelectorAll(".result_currency");

    result_currency_all.forEach((result_currency) => {
      result_currency.innerHTML = Math.round(
        result * result_currency.dataset.value
      );
    });
  }
}
