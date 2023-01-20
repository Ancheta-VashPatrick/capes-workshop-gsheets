/* 
    sets active css for navbar menu based on corresponding active page 
*/
$(document).ready(function(){
    var url = window.location.pathname;
    if (url.indexOf("oportal") != -1) url = '/oportal/';
    $('ul li a[href="' + url + '"]').addClass('active');
    $('ul li a[href="' + url + '"]').css('background-color', 'gray');
    console.log(url)
});