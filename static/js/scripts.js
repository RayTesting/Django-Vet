/*

    const -> constantes, no cambian valor, se usan para funciones
    let -> variables, pueden cambiar de valor
    var -> lo mismo que el let pero no se debe usar

    1. function nombre(){

    }

    2. const myFunction = function(){

    }

    3. const myFunction = () => (
        console.log('hello)
    )

*/

//navbar settings
const navButton = document.getElementById('nav_button')
const navButtonIcon = document.getElementById('nav_button_icon')
const navLinks = document.getElementById('nav_links')

const userButton = document.getElementById('user_button')
const userLinks = document.getElementById('user_links')

navButton?.addEventListener('click', () => {
    navLinks.classList.toggle('hidden')
    navButtonIcon.classList.toggle('bi-x-lg')
})

const handleWindowSize = () => {
    if (window.innerWidth >= 768){
        if (navLinks.classList.contains('hidden')){
            navLinks.classList.remove('hidden')
            if(!navButtonIcon.classList.contains('bi-x-lg')){
              navButtonIcon.classList.add('bi-x-lg')
            }
        }
    }
}

userButton?.addEventListener('click', () => {
    userLinks.classList.toggle('hidden')
})

window.onresize = handleWindowSize
window.onload = handleWindowSize


const swiper = new Swiper('.swiper', {
    // Optional parameters
    autoplay: {
        delay: 5000,
      },
    loop: true,
  
    effect: 'fade',
    fadeEffect: {
      crossFade: true
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });
  
const swiperItems = new Swiper('.swiper-items', {
    // Optional parameters
    autoplay: {
        delay: 5000,
      },
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
    breakpoints: {
      
      640: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView:3,
      }
    }
  });
