document.addEventListener('DOMContentLoaded', function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('LI').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('LI').remove();
  });
});
