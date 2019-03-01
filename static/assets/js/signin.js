var googleUser = {};
var startSigninButton = function() {
  gapi.load('auth2', function(){
    // Retrieve the singleton for the GoogleAuth library and set up the client.
    auth2 = gapi.auth2.init({
      <!-- [END pre-client_id] -->
      client_id: '239280034936-ff73cf0a91k15b950c393d2rls332nqu.apps.googleusercontent.com',
      <!-- [START post-client_id] -->
      cookiepolicy: 'single_host_origin',
      // Request scopes in addition to 'profile' and 'email'
      //scope: 'additional_scope'
    });
    //attachSignin(document.getElementById('google-signin'));
  });
};

function attachSignin(element) {
  console.log(element.id);
  auth2.attachClickHandler(element, {},
    function(googleUser) {
      document.getElementById('google-signin').innerText = "Sign out";
      var auth = googleUser.getAuthResponse().id_token;
      var profile = googleUser.getBasicProfile();
      var csrf_tok = jQuery("[name=csrfmiddlewaretoken]").val(); 
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrf_tok);
          }
        }
      });
      $.ajax({
        type: "POST",
        url: "/login/oauth_success",
        data: {
          "idtoken" : profile.getId(),
          "name"    : profile.getName(),
          "email"   : profile.getEmail(),
        }
      });
    }, function(error) {
    });
}

