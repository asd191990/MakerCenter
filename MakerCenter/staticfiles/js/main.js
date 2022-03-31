$(function () {
    // nav 用
    $(document).scroll(function () {
        let $nav = $('.sticky-top');
        let $header_bg_height = $('.header-bg').height();
        if($(this).scrollTop() > $header_bg_height){
            $nav.addClass('scrolled');
            $('.nav-link').removeClass('text-dark');
            $('.nav-link').addClass('text-white');
        }else{
            $nav.removeClass('scrolled');
            $('.nav-link').removeClass('text-white');
            $('.nav-link').addClass('text-dark');
        }
    });
});