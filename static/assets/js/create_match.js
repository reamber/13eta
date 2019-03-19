$(document).ready(function(){
  var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
  console.log("attaching");
  $(this).find( ".matchbutton" ).click(function() {
    console.log("sending");
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
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
});
