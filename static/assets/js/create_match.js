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
    var button = $(this);
    var result = $.ajax({
      type: "POST",
      url: "/match/creatematch",
      data: {
        "matchID" : UserID
      },
      complete: function(data){
        console.log(data.responseText);
        if(data.responseText==="Match created"){
          button.html("Match Pending<br/>Unmatch?");
          button.css("background","orange");
        }else if(data.responseText==="Match Already Exists"){
          button.html("Match Pending<br/>Unmatch?");
          button.css("background","orange");
        }
      }
    });
  });
});
