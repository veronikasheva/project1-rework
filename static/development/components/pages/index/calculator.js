import './calculator.scss'
import validation from "../../module/validation"

const calculator_btn = document.querySelector('.calculator__btn > button')

calculator_btn.addEventListener('click', calculate)

function calculate(e) {
    e.preventDefault()
    const status = validation(calculator_btn)

    const excise = ({engine, year, fuel}) => {
        console.log(year);
        const current_year = new Date().getFullYear()

        const cff_engine = engine / 1000
        const cff_year = current_year - year > 15 ? 15 : current_year - year

        const rate = (engine >= +fuel.dataset.lim) ? +fuel.dataset.max_rate : +fuel.dataset.min_rate

        return rate * cff_engine * cff_year
    }

    if (status) {
        const price = +document.querySelector('input[name="price"]').value
        const currency = +document.querySelector('input[name="currency"]:checked').dataset.value
        const engine = +document.querySelector('input[name="engine"]').value
        const year = +document.querySelector('select[name="year"]').value

        const fuel_select = document.querySelector('select[name="fuel"]')
        const fuel_selected_index = fuel_select.selectedIndex
        const fuel = fuel_select.querySelectorAll('option')[fuel_selected_index]

        const excise_result = fuel.value === 'hybrid' ? 100 : excise({engine, year, fuel})
        const toll = (price / currency) * 10 / 100
        const pdv = ((price / currency) + excise_result + toll) * 20 / 100

        const result = excise_result + toll + pdv
        const result_currency_all = document.querySelectorAll('.result_currency')

        result_currency_all.forEach(result_currency => {
            result_currency.innerHTML = Math.round(result * result_currency.dataset.value)
        })
    }
}


