document.addEventListener('DOMContentLoaded', function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (result) { $('DIV#hello').text(result.hello); });
});
