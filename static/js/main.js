import $ from 'jquery';

$(document).ready(() => {
    const $div = $('.hello-world');
    $div.mouseenter((e) => {
        $(e.currentTarget).addClass('hello-world-hover');
    });
    $div.mouseleave((e) => {
        $(e.currentTarget).removeClass('hello-world-hover');
    });
});
