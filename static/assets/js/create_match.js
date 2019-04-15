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
    var view = "/match/creatematch"
    if(button.text() === "Match PendingUnmatch?" || button.text() === "MatchedUnmatch?"){
      view = "/match/removematch"
    }
    var result = $.ajax({
      type: "POST",
      url: view,
      data: {
        "matchID" : UserID
      },
      complete: function(data){
        console.log(data.responseText);
        if(data.responseText==="Match created"){
          button.html("Match Pending<br/>Unmatch?");
          button.css("background","orange");
          button.css("line-height","");
        }else if(data.responseText==="Match Already Exists"){
          button.html("Match Pending<br/>Unmatch?");
          button.css("background","orange");
          button.css("line-height","");
        }else if(data.responseText==="Match removed"){
          button.html("Match");
          button.css("background","");
          button.css("line-height","48px");
        }else if(data.responseText==="Match completed"){
          button.html("Matched<br/>Unmatch?");
          button.css("background","green");
          button.css("line-height","");
        }
      }
    });
  });
});
