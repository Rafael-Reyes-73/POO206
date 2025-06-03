const menuTwo = document.querySelector('.side-menu');
const button = document.querySelector('#toggle_open');
const close_btn = document.querySelector('#toggle_close');

button.addEventListener('click', () => {
    menuTwo.classList.toggle('active');
});
menuTwo.addEventListener('click', () => {
    menuTwo.classList.toggle('active');
});



const menu_toggle = document.querySelector('#menu_bars'); 
const menuOne = document.querySelector('.menu'); 

menu_toggle.addEventListener('click' , () =>{
    menuOne.classList.toggle('show_menu');
});

var swiper = new Swiper('.mySwiper', {
    spaceBetween: 30,
    effect: "fade",
    loop: true,
    autoplay: true,
});



var swiper = new Swiper('.serviceSwiper', {
    slidesPerView: 3, 
    spaceBetween: 30, 
    autoplay: true,
    loop: true,
    breakpoints: {
        0: {
            slidesPerView: 1,
            spaceBetween: 10, 
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 20, 
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 30, 
        },
    },
});

