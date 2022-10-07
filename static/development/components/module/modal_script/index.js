import './index.scss'


let modal_open = document.querySelectorAll('.modal_open');
let all_modals = document.querySelectorAll('.modal__block');
let modal_close = document.querySelectorAll('.modal_close');
modal_open.forEach(element => {
    let modal_block = document.querySelector(`.${element.dataset.href}`);
    element.addEventListener('click', function () {
        all_modals.forEach(modal => {
            modal.classList.remove('active');
        });
        modal_block.classList.add('active');
    });

});


all_modals.forEach(element => {
    document.body.addEventListener('click', e => { // при клике в любом месте окна браузера
        const target = e.target // находим элемент, на котором был клик
        let check = element.classList.contains('active');

        if (!target.closest('.modal__block') && !target.closest('.modal_open') && check) { // если этот элемент или его родительские элементы не окно навигации и не кнопка
            element.classList.remove('active') // то закрываем окно навигации, удаляя активный класс
        }
    })
});


modal_close.forEach(element => {
    let wrapper = element.closest('.modal__block');
    element.addEventListener('click', function () {
        wrapper.classList.remove('active');
    })
});
