$(function () {

    var menu = $("#menu"),
        headerH = $("#header").innerHeight(),
        scrollOffset = $(window).scrollTop();
    
    /* Fixed Menu */
    checkScroll(scrollOffset)
    
    $(window).on("scroll", function() {
        scrollOffset = $(this).scrollTop();

        checkScroll(scrollOffset)

    });

    function checkScroll(scrollOffset) {

        if( scrollOffset >= headerH ) {
            menu.addClass("fixed");
        } else {
            menu.removeClass("fixed");
        }
    }

    /* Smooth scroll */
    $("[data-scroll]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('scroll'), 
            blockOffset = $(blockId).offset().top - 80;

        $("#nav a").removeClass("active");
        $this.addClass("active");

        if ($("#nav_toggle").hasClass('active')) {
        
            $(window).on("scroll", function() {

            $('#nav_toggle').removeClass("active");

            $("#nav").removeClass("active");

            });
        }
        
        
        $("html, body").animate({
            scrollTop: blockOffset
        }, 500);
    });

    /* Menu nav Toggle */
    $("#nav_toggle").on("click", function(event) {
        event.preventDefault();
        
        $(this).toggleClass("active");
        $("#nav").toggleClass("active");
    });

    $("[data-slider]").slick( {
        infinite: true,
        fade: false,
        slidesToShow: 1,
        slidesToScroll: 1
    });

    // вешаем маску на телефон
    $('.phone-field').inputmask("+372 9999 9999");

    // добавляем правило для валидации телефона
    jQuery.validator.addMethod("checkMaskPhone", function(value, element) {
        return /\+\d{3}\ \d{4}\ \d{4}/g.test(value); 
    });
    
    // получаем нашу форму по class
    var form = $('.form-request');
    
    // включаем валидацию в форме
    form.validate();
    
    // вешаем валидацию на поле с телефоном по классу
    $.validator.addClassRules({
        'phone-field': {
            checkMaskPhone: true,
        }
    });
    
    // Проверка на валидность формы при отправке, если нужно
    form.submit(function(e){
        if (form.valid()) {
            alert('Форма отправлена');
        }
        return;
    });

});