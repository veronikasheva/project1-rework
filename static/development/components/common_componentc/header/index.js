import './index.scss'

let hamburger = document.querySelector('#hamburger')
let header = document.querySelector('.header')

hamburger.addEventListener('click', () => header.classList.toggle('active'))

const navigation = header.querySelector('.nav')

navigation.addEventListener('click', (e) => {
    if (header.classList.contains('active') && e.target.tagName === 'A') {
        header.classList.remove('active')
    }
})