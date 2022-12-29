import bottle
import json
import data


@bottle.route("/")
def main_page():
  response = bottle.static_file("login.html", root=".")
  return response


@bottle.route("/script.js")
def script():
  response = bottle.static_file("script.js", root=".")
  return response


@bottle.route("/ajax.js")
def ajax():
  response = bottle.static_file("ajax.js", root=".")
  return response


@bottle.route("/style.css")
def style():
  response = bottle.static_file("style.css", root=".")
  return response


@bottle.route("/login.html")
def login_html():
  response = bottle.static_file("login.html", root=".")
  return response


@bottle.route("/signup.html")
def signup_html():
  response = bottle.static_file("signup.html", root=".")
  return response


@bottle.post("/login")
def login():
  response = json.loads(bottle.request.body.read().decode())
  return json.dumps(data.check_creds(response[0], response[1]))


@bottle.post("/signup")
def signup():
  response = json.loads(bottle.request.body.read().decode())
  return json.dumps(data.add_account(response[0], response[1]))


bottle.run(host="0.0.0.0", port=8080)
