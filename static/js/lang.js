$(document).ready(function() {

   $('.ru').on('click', function() {
      var r = $('.localization').each(function() {
         var el = $(this);
         var key = (el.attr('caption'));
         el.text(rus[key]);
      });
   });


   $('.en').on('click', function() {
      var r = $('.localization').each(function() {
         var el = $(this);
         var key = (el.attr('caption'));
         el.text(eng[key]);
      });
   });


   $('.ge').on('click', function() {
      var r = $('.localization').each(function() {
         var el = $(this);
         var key = (el.attr('caption'));
         el.text(eng[key]);
      });
   });


   var rus = {
      test: 'тест',
      name: 'имя'
   };
   var eng = {
      test: 'test',
      name: 'name'
   };


});