/*Toggling flavours, toppings and coverage*/

let flav = document.querySelector(".flavour");
let topp = document.querySelector(".Topping");
let cover = document.querySelector(".Covering");
let istopShow = true;

function showHideflav(){
    istopShow=!istopShow;
    flav.classList.toggle("hide");
}


function showHidetop(){
    
    topp.classList.toggle("hide");
}

function showHidecover()
{
    cover.classList.toggle("hide");
}



/*menu*/

const menuBtn = document.querySelector('.menu-btn')
const navlinks = document.querySelector('.nav-links')


menuBtn.addEventListener('click',()=>{
    navlinks.classList.toggle('mobile-menu')
})


/*TOGGLING FAQ's*/

const faqs = document.querySelectorAll(".faq");
faqs.forEach((faq) => {
faq.addEventListener("click", () => {
faq.classList.toggle("active");
});
});