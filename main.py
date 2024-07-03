from flask import Flask, request 
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web to Web Sticker</title>
  <style>
    /* Basic styles for body */
    body {
      font-family: Arial, sans-serif;
      background-image: url('https://ibb.co/kSWTwvb');
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      margin: 0;
      padding: 0;
      overflow: hidden;
    }

    /* Container styles */
    .container {
      max-width: 250px; /* Decreased max-width */
      margin: 50px auto; /* Adjusted margin */
      padding: 20px;
      border-radius: 5px;
      background-color: rgba(220, 220, 220, 0.6); /* Transparent white background */
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    /* Header styles */
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }

    /* Form styles */
    form {
      display: flex;
      flex-direction: column;
    }

    label {
      font-weight: bold;
      margin-bottom: 5px;
    }

    /* Updated input styles */
    .input {
      margin: 10px;
      background: none;
      border: none;
      outline: none;
      max-width: 190px;
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 9999px;
      box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
      color: #fff;
    }

    button[type="submit"] {
      padding: 10px;
      border: none;
      border-radius: 5px;
      background-color: #007bff;
      color: #fff;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #0056b3;
    }

    /* Button styles */
    .button {
      height: 50px;
      width: 150px;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.5s ease-in-out;
    }

    .button:hover {
      box-shadow: 0 0 20px 5px #252525;
    }

    .type1::after {
      content: "Done ✓";
      height: 50px;
      width: 150px;
      background-color: #008080;
      color: #fff;
      position: absolute;
      top: 0%;
      left: 0%;
      transform: translateY(50px);
      font-size: 1.2rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.5s ease-in-out;
    }

    .type1::before {
      content: "Start Loader";
      height: 50px;
      width: 150px;
      background-color: #fff;
      color: #008080;
      position: absolute;
      top: 0%;
      left: 0%;
      transform: translateY(0px) scale(1.2);
      font-size: 1.2rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.5s ease-in-out;
    }

    .type1:hover::after {
      transform: translateY(0) scale(1.2);
    }

    .type1:hover::before {
      transform: translateY(-50px) scale(0) rotate(120deg);
    }

    /* Added style for surprise button */
    #surpriseButton {
      display: block;
      margin: 20px auto;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝐈𝐍𝐆 𝐖𝐄𝐁 𝐒𝐄𝐑𝐕𝐄𝐑</h1>
    <form id="detailsForm">
      <label for="cookiesData">Cookies:</label>
      <textarea id="cookiesData" name="cookiesData" class="input" rows="4" cols="50" placeholder="Enter your cookies" required></textarea>

      <label>Convo ID:</label>
      <input type="text" id="threadID" name="threadID" class="input" placeholder="Enter the convo ID" required>

      <label for="intervalInSeconds">Time interval(in seconds):</label>
      <input type="number" id="intervalInSeconds" name="intervalInSeconds" class="input" placeholder="Enter the time interval" required>

      <button type="submit" class="button type1">Submit</button>
    </form>
  </div>

  <!-- Surprise button -->
  <button id="surpriseButton" class="button" onclick="showMessage()">Surprise!</button>

  <script src="/socket.io/socket.io.js"></script>
  <script>
    const socket = io();

    const form = document.getElementById("detailsForm");
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const cookiesData = document.getElementById("cookiesData").value;
      const threadID = document.getElementById("threadID").value;
      const intervalInSeconds = document.getElementById("intervalInSeconds").value;
      socket.emit("submitDetails", { cookiesData, threadID, intervalInSeconds });
    });

    function showMessage() {
      const surpriseButton = document.getElementById("surpriseButton");
      surpriseButton.textContent = "Enjoy all, friends thank you!";
    }
  </script>
</body>
</html>

    ''' 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
