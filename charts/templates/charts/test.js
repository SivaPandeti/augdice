$.getJSON('https://api.dice.com/jobs?fields=id,company,position&page=1&q=ruby', function(data) {
    console.log(data);
});

/*
$.ajax({
  dataType: "json",
  url: "https://api.dice.com/jobs?fields=id,company,position&page=1&q=ruby",
  data: ,
  success: success
});