$(document).ready(function() {
    $('.js--events').waypoint(function(direction) {
        if (direction == "down") {
            $('nav').addClass('sticky');
        } else {
            $('nav').removeClass('sticky');
        }
    }, {
      offset: '60px;'
    });

    $('.js--scroll-to-about').click(function () {
        $('html, body').animate({scrollTop: $('.js--events').offset().top}, 1000);
    });

    $('.js--scroll-to-sponsors').click(function () {
        $('html, body').animate({scrollTop: $('.js--sponsors').offset().top}, 1000);
    });

    $('.js--scroll-to-gallery').click(function () {
        $('html, body').animate({scrollTop: $('.js--gallery').offset().top}, 1000);
    });

    $('.js--scroll-to-contact').click(function () {
        $('html, body').animate({scrollTop: $('.js--contact').offset().top}, 1000);
    });

    $('.js--scroll-to-top').click(function () {
        $('html, body').animate({scrollTop: $('.js--top').offset().top}, 1000);
    });

    $('.js--events').waypoint(function(direction) {
        $('.js--wp-1').addClass('animated fadeIn');
        $('.container').addClass('animated pulse');
    });

    $('.thing').slick({
        dots: false,
        arrows: true,
        autoplay: true,
        autoplaySpeed: 3000
    });

    $('.js--nav-icon').click(function() {
        var nav = $('.js--main-nav');
        var icon = $('.js--nav-icon i');
        if(icon.hasClass('ion-android-menu')) {
            icon.addClass('ion-android-close');
            icon.removeClass('ion-android-menu');
        } else {
            icon.removeClass('ion-android-close');
            icon.addClass('ion-android-menu');
        }
        nav.slideToggle(200);
    });

    $(window).on("load",function(){
        $(".loader-wrapper").fadeOut("slow");
      });
}); 