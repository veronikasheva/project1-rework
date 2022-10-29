import './index.scss'
import './calculator'

fetch('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
    .then(response => {
        return response.json()
    })
    .then(data => {
        const usd = data.find(currency => currency.cc === "USD")
        const eur = data.find(currency => currency.cc === "EUR")
        const cad = data.find(currency => currency.cc === "CAD")

        const curse_usd = document.querySelector('#curse_usd')
        const curse_euro = document.querySelector('#curse_euro')
        const curse_cad = document.querySelector('#curse_cad')

        curse_usd.innerHTML = usd.rate
        curse_euro.innerHTML = eur.rate
        curse_cad.innerHTML = cad.rate

        const ratio_usd = eur.rate / usd.rate
        const ratio_cad = eur.rate / cad.rate
        const ratio_uan = eur.rate

        const result_usd = document.querySelectorAll('.cff_usd')
        const result_cad = document.querySelectorAll('.cff_cad')
        const result_uan = document.querySelectorAll('.cff_uan')

        result_usd.forEach(usd => usd.dataset.value = ratio_usd)
        result_cad.forEach(usd => usd.dataset.value = ratio_cad)
        result_uan.forEach(usd => usd.dataset.value = ratio_uan)
    })