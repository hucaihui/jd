
// Login form resize
function loginResize() { 
    var windowWidth = $(window).width();
    var formwidth = $('.login').width();

    $(".login").css('left', (windowWidth / 2) - (formwidth / 2)).css('position', 'relative');
}



$(document).ready(function () {
	loginResize();					// initate Login form resize 
	$(window).resize(function () {    
		loginResize();
	});
});