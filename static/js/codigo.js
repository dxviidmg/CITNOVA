$("#link-inicio").click(function() {
    $('html, body').animate({
        scrollTop: $("#inicio").offset().top
    }, 2000);
});

$("#link-inicio2").click(function() {
    $('html, body').animate({
        scrollTop: $("#inicio").offset().top
    }, 2000);
});

$("#link-sobre-mi").click(function() {
    $('html, body').animate({
        scrollTop: $("#sobre-mi").offset().top
    }, 2000);
});

$("#link-portafolio").click(function() {
    $('html, body').animate({
        scrollTop: $("#portafolio").offset().top
    }, 2000);
});

$("#link-publicaciones").click(function() {
    $('html, body').animate({
        scrollTop: $("#publicaciones").offset().top
    }, 2000);
});

$("#link-comunidades").click(function() {
    $('html, body').animate({
        scrollTop: $("#comunidades").offset().top
    }, 2000);
});

$("#link-galeria").click(function() {
    $('html, body').animate({
        scrollTop: $("#galeria").offset().top
    }, 2000);
});

$("#link-contacto").click(function() {
    $('html, body').animate({
        scrollTop: $("#contacto").offset().top
    }, 2000);
});


$('.thumbnail').click(function(){
      $('.modal-body').empty();
    var title = $(this).parent('a').attr("title");
    $('.modal-title').html(title);
    $($(this).parents('div').html()).appendTo('.modal-body');
    $('#myModal').modal({show:true});
});