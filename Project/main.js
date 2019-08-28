$(function(){
   $(window).resize(function(){
    if($(window).width() <= 770 && !$("#wrapper").hasClass('toggled')){
    	$("#wrapper").addClass("toggled");
    }else if($("#wrapper").hasClass('toggled')){
    	$("#wrapper").removeClass("toggled");
    }
}); 
});