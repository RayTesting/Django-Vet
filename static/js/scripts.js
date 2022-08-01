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



navButton.addEventListener('click', () => {
    navLinks.classList.toggle('hidden')
    navButtonIcon.classList.toggle('bi-x')
} )


const handleWindowSize = () => {
    if(window.innerWidth >= 768){
        if(navLinks.classList.contains('hidden')){
            navLinks.classList.remove('hidden')
        }
    }
}

window.onresize = handleWindowSize
window.onload = handleWindowSize



//swiper//
const swiper = new Swiper('.swiper', {
    speed: 400,
    spaceBetween: 10,
    autoplay:{
        delay:5000
    },
    loop: true,
    effect: 'fade',
    fadeEffect: {
        crossFade:true
    },
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    pagination: {
        el: '.swiper-pagination'
    }
  });
//swiper//