import Swiper, {
    Autoplay,
    Navigation,
    Pagination,
    Scrollbar
} from 'swiper';
import 'swiper/swiper-bundle.css'
import './index.scss'

Swiper.use([Autoplay, Navigation, Pagination, Scrollbar])

const banner = new Swiper(".banner", {
    slidesPerView: '1',
    loop: true,
    spaceBetween: 30,

    navigation: {
        nextEl: ".top-slider-btn-next",
        prevEl: ".top-slider-btn-prev",
    },

    pagination: {
        el: ".banner-pagination",
        type: "fraction",
        renderFraction: function (currentClass, totalClass) {
            return `<div class="pagination_wrapper"> 
                <span class="currentZero">0</span><span class="${currentClass}"></span> 
                <span class="totalZero">/0</span><span class="${totalClass}"></span> 
            </div>`
        }
    },
})

const partners_swiper = new Swiper(".partners_swiper", {
    spaceBetween: 10,
    pagination: {
        el: ".partners-pagination",
        type: "progressbar"
    },
    breakpoints: {
        1000: {
            slidesPerView: 4,
        },
        700: {
            slidesPerView: 3,
        },
        400: {
            slidesPerView: 2,
        },
        300: {
            slidesPerView: 1.5,
        }
    }
})

const about_services = new Swiper('.about_services', {
    slidesPerView: '4',
    spaceBetween: 15,
    breakpoints: {
        1000: {
            slidesPerView: 4,
        },
        700: {
            slidesPerView: 3,
        },
        400: {
            slidesPerView: 2,
        },
        300: {
            slidesPerView: 1.5,
        }
    }
})