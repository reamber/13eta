
$( ".matchbutton" ).click(function() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_tok);
      }
    }
  });
  var result = $.ajax({
    type: "POST",
    url: "/match/creatematch",
    data: {
      "matchID" : $(this).parent().(".userID").text()
    },
    complete: function(data){

    }
  });
});

