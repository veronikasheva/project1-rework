import './index.scss'

let hamburger = document.querySelector('#hamburger')
let header = document.querySelector('.header')

hamburger.addEventListener('click', () => header.classList.toggle('active'))