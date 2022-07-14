console.log("helo");
/* --------------show pass rules -------- */
$("#id_password1").focus(function(){
    $(".cust-form ul").css("display", "block").slideDown();
  });

$("#id_password1").focusout(function(){
$(".cust-form ul").css("display", "none").slideUp();
});


/* -------------- */
