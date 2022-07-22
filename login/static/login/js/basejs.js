console.log("helo");
/* --------------show pass rules -------- */
$("#id_password1").focus(function(){
    $(".cust-form ul").css("display", "block").slideDown();
  });

$("#id_password1").focusout(function(){
$(".cust-form ul").css("display", "none").slideUp();
});


/* ------------sidebar------- */
function toggleSidebar(){
  if ($('.sidebar').css('display') == 'none') {
    $('.sidebar').css('display', 'block');
  }
  else {
    $('.sidebar').css('display','none');
  }
}

window.onresize = function(event) {
  const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)
  console.log('resize');
  if(vw > 630){
    console.log('big size');
    $('.sidebar').css('display','none');
  }
};