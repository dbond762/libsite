document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.header__bars').addEventListener('click', () => {
        document.querySelector('.header__menu').classList.toggle('header__menu--collapsed');
    });
});
