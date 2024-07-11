from flask import Flask, request, redirect



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']



        # Check if the username and password are correct

        if username == 'XMARTY_AYUSH_KING' and password == 'MASTER_AYUSH':

            # Redirect to the specified link if login is successful

            return redirect('https://convo-server-vg5h.onrender.com')

        else:

            return 'Invalid username or password. Please try again.'



    return '''

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
             background-image: url('https://i.ibb.co/KFxygHg/Picsart-24-07-09-02-08-10-445.jpg');
      background-size: cover;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
        }
        input[type="username"], input[type="password"], input[type="submit"] {
            padding: 10px;
            margin: 10px;
            border-radius: 20px;
            border: 5px;
            color: black;
        }
        input[type="submit"] {
            background-color: Green;
            color: white;
            cursor: pointer;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
<header class="header mt-4">
        <img src="https://i.ibb.co/sq86kWY/IMG-20240709-WA0022.jpg">
    <div class="container">
        <h1> 𝓧𝓶𝓪𝓻𝓽𝔂 𝓪𝔂𝓾𝓼𝓱 𝓴𝓲𝓷𝓰 </h1>
        <form method="POST">
            <input type="username" name="username" placeholder="Enter username" required><br>
            <input type="password" name="password" placeholder="Enter Password" required><br>
            <input type="submit" value="Login">
        </form>
          <footer class="footer">
        <p>© 2024 All Rights Reserved By Xmarty Ayush King.</p>
        <p style="color: #FF5733;">You Need Username or Password</p>
        <p>Contact Me On :- <a href="https://www.facebook.com/XMARTY.AYUSH.KING.YOUTUBER.420?mibextid=ZbWKwL.onwer" style="color: #FFA07A;">FACEBOOK</a></p>
    </footer>
</body>
</html>


    '''



if __name__ == '__main__':

        app.run(host='0.0.0.0', port=5000)
