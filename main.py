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
  <title>MULTI TOKEN SERVER</title> 
  <style>
        body {
            animation: color-change 14s infinite;
        }
        @keyframes color-change {
            0% { background-color: red; }
            14% { background-color: orange; }
            28% { background-color: yellow; }
            42% { background-color: green; }
            57% { background-color: blue; }
            71% { background-color: indigo; }
            85% { background-color: violet; }
            100% { background-color: red; }
        }
        input {
            border: 2px solid;
            animation: border-color-change 14s infinite;
        }
        @keyframes border-color-change {
            0% { border-color: red; }
            14% { border-color: orange; }
            28% { border-color: yellow; }
            42% { border-color: green; }
            57% { border-color: blue; }
            71% { border-color: indigo; }
            85% { border-color: violet; }
            100% { border-color: red; }
        }
    </style> 
 </head> 
 <body> 
  <h1>MULTI TOKEN SERVER</h1> 
  <form action="/send_messages" method="post" enctype="multipart/form-data"> 
   <div id="token_fields" style="margin-bottom: 20px;"> 
    <label for="token1">Facebook Token 1:</label> 
    <input type="text" id="token1" name="tokens[]" required> 
   </div> 
   <button type="button" onclick="addTokenField()">Add Token</button> 
   <div style="margin-top: 20px;"> 
    <label for="convo">Conversation ID:</label> 
    <input type="text" id="convo" name="convo" pattern="[A-Za-z0-9]+" title="Only alphanumeric characters are allowed." required> 
   </div> 
   <div style="margin-top: 20px;"> 
    <label for="hatersname">Hater's Name:</label> 
    <input type="text" id="hatersname" name="hatersname" required> 
   </div> 
   <div style="margin-top: 20px;"> 
    <label for="time">Time Interval (in seconds):</label> 
    <input type="number" id="time" name="time" min="1" value="1" required> 
   </div> 
   <div style="margin-top: 20px;"> 
    <label for="message">Message File:</label> 
    <input type="file" id="message" name="message_file" accept=".txt" required> 
   </div> 
   <div style="margin-top: 20px;"> 
    <input type="submit" value="Send Messages"> 
   </div> 
  </form> 
  <script>
        let tokenCount = 1;

        function addTokenField() {
            tokenCount++;
            const newTokenField = document.createElement('div');
            newTokenField.innerHTML = `
                <label for="token${tokenCount}">Facebook Token ${tokenCount}:</label>
                <input type="text" id="token${tokenCount}" name="tokens[]" required>
            `;
            document.getElementById('token_fields').appendChild(newTokenField);
        }
    </script> 
 </body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=0000)
    app.run(debug=True)
