function get_val() {
  let username = document.getElementById("l_user").value;
  let password = document.getElementById("l_pass").value;
  let account = [username,password];
  ajaxPostRequest("/login",JSON.stringify(account),temp);
}

function temp(inp) {
  let messsage = document.getElementById("message");
  message["innerHTML"] = inp
}

function s_get_val() {
  let username = document.getElementById("s_user").value;
  let password = document.getElementById("s_pass").value;
  let account = [username,password];
  ajaxPostRequest("/signup",JSON.stringify(account),s_temp);

  
}

function s_temp(inp) {
  let messsage = document.getElementById("s_message");
  messsage["innerHTML"] = JSON.parse(inp)
}
