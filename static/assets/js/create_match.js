
$( ".matchbutton" ).click(function() {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrf_tok);
      }
    }
  });
  var UserID = $(this).parent().find(".userID").text();
  var result = $.ajax({
    type: "POST",
    url: "/match/creatematch",
    data: {
      "matchID" : UserID
    },
    complete: function(data){

    }
  });
});

