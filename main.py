from flask import Flask, request, redirect



app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']



        # Check if the username and password are correct

        if username == 'AYUSH_KING' and password == 'KING_899':

            # Redirect to the specified link if login is successful

            return redirect('https://multy-convo.replit.app/')

        else:

            return 'Invalid username or password. Please try again.'



    return '''

    <html>

    <head>

        <style>

        body {

         background-image: url('https://i.ibb.co/D91X2tp/748589c805ed5b31a1e33a28d5f1ba0c.jpg');  
      background-size: cover;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;

    }

    body {

      font-family: Arial, sans-serif;

    }




    .container label, .container input[type="text"], .container input[type="password"] {

      display: block;

      width: 100%;

      margin-bottom: 10px;

    }



    .container button {

      width: 100%;

      padding: 10px;

      background-color: #4CAF50;

      color: white;

      border: none;

      cursor: pointer;

    }



    .container button:hover {

      background-color: #45a049;

    }

  </style>

    </head>

    <body>

        <div class="container">
          <header class="header mt-4">
    <h1 class="mb-3">♛┈⛧𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝐈𝐍𝐆⛧┈♛
    <h1 class="mt-3">        𝐎𝐅𝐅𝐋𝐈𝐍𝐄  𝐂𝐎𝐍𝐕𝐎 𝐒𝐄𝐑𝐕𝐄𝐑
    <h1 class="mt-3"> 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐎𝐖𝐍𝐄𝐑 𝐓𝐎 𝐆𝐄𝐓 𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄 𝐎𝐑 𝐏𝐀𝐒𝐒 </h1>
  </header>


            <h1 style="color: white;"> 𝐒𝐔𝐁𝐌𝐈𝐓 𝐀𝐋𝐋 𝐃𝐄𝐓𝐓𝐀𝐈𝐋𝐒 </h1>

            <form method="POST" action="/">

                <div class="form-group">

                    <label for="username "style="color: white;">𝐄𝐍𝐓𝐄𝐑 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄:</label>

                    <input type="text" id="username" name="username" required>

                </div>

                <div class="form-group">

                    <label for="password"style="color: white;">𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃:</label>

                    <input type="password" id="password" name="password" required>

                </div>

                <button type="submit" class="btn">Login</button>

            </form>

            <div class="random-images">
        <img src="https://i.ibb.co/D91X2tp/748589c805ed5b31a1e33a28d5f1ba0c.jpg" alt="Random Image 1" class="random-img">
        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">
        <p>© 2024 All Rights Reserved By Ak.</p>
        <p style="color: #FF5733;">Convo/Inbox Loader Tool</p>
        <p>XMARTY AYUSH KING<a href="https://www.facebook.com/XMARTYAYUSHKING" style="color: #FFA07A;">FACEBOOK</a></p>
    </footer>
</body>
</html>

    '''



if __name__ == '__main__':

        app.run(host='0.0.0.0', port=5000)
        app.run(host='0.0.0.0', port=port)
        app.run(debug=True)
