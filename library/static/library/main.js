document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.header__bars').addEventListener('click', () => {
        document.querySelector('.header__menu').classList.toggle('header__menu--collapsed');
    });

    let categories = document.querySelectorAll('.category-list__item');
    for (let item of categories) {
        item.addEventListener('click', () => {
            document.querySelector('.category-list__active-item').value = item.dataset.id;
            document.querySelector('.category-list__form').submit();
        });
    }
});
