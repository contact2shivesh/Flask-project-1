
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login </title>
    
    <link rel="icon" href="{{ url_for('static', filename='assets/favicon.ico') }}">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    
<style>
       
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.login-container {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  text-align: center;
}

h2 {
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input[type="text"], input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.login-button {
  width: 100%;
  padding: 10px;
  background-color: #5cb85c;
  border: none;
  border-radius: 4px;
  color: white;
  font-size: 16px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #4cae4c;
}
</style>
</head>
{% with messages = get_flashed_messages(with_categories=True) %}
      
        <ul>
          {% for category, message in messages %}
            <li class="alert alert-{{ info }}">{{ message }}</li>
          {% endfor %}
        </ul>
     
    {% endwith %}
<body>
    <div class="login-container">
    {% set fname =  params['login_image']  %}
      <img class="mb-4" src="{{url_for('static', filename=fname)}}" alt="" width="72" height="72">
              <h2>Login</h2>
        <form action="/dashboard" method="post">
            <div class="input-group">
                <label for="uname">User Name</label>
                <input type="text" id="uname" name="uname" required>
            </div>
            <div class="input-group">
                <label for="pass">Password</label>
                <input type="password" id="pass" name="pass" required>
                <label>
                <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <button type="submit" class="login-button">Login</button>
            <p class="mt-5 mb-3 text-muted">© {{params['headName'] }} 2024</p>
        </form>
    </div>
</body>
</html>

