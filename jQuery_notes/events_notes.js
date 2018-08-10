
// Examples

// $("h1").click(function(){
//   $(this).text("This is changed on click.")
// })


// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue');
// })


// $('input').eq(0).keypress(function(event){
//   if (event.which === 13) {
//     $('h3').toggleClass('turnBlue');
//   }
// })
//
// // on method is like eventlistener
// $('h1').on('dblclick',function(){
//   $(this).toggleClass('turnBlue');
// })



$('input').eq(1).on('click',function(){
  $('.container').fadeOut(3000);
})
