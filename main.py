pp.run(host='0.0.0.0', port=5000)from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_event = Event()
threads = []

def send_messages(access_tokens, thread_id, mn, time_interval, messages):
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message sent using token {access_token}: {message}")
                else:
                    print(f"Failed to send message using token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global threads
    if request.method == 'POST':
        token_file = request.files['tokenFile']
        access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        if not any(thread.is_alive() for thread in threads):
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages))
            threads.append(thread)
            thread.start()

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝐈𝐍𝐆</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    body{
      background-color: #f8f9fa;
    }
    .container{
      max-width: 500px;
      background-color: #fff;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h2 class="mb-3">☠ ||| ꜱᴇʀᴠᴇʀ ᴀᴄᴛɪᴠᴇ ||| ☠</h2>
    <img src="/static/images/logo.jpg" alt="𝐎𝐅𝐅𝐋𝐈𝐍𝐄 𝐑𝐔𝐋𝐄𝐗" width="300px">
    <h1 class="mt-3">♛ 𝐎𝐖𝐍𝐄𝐑 : 𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝟏𝐍𝐆♛ </h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">𝐒𝐄𝐋𝐄𝐂𝐓 𝐘𝐎𝐔𝐑 𝐓𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝐆𝐑𝐎𝐔𝐏 + 𝐈𝐍𝐁𝐎𝐗 𝐍𝐔𝐌𝐁𝐄𝐑</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝐄𝐍𝐓𝐄𝐑 𝐇𝐀𝐓𝐓𝐄𝐑𝐒 𝐍𝐀𝐌𝐄</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝐌𝐄𝐒𝐒𝐄𝐆𝐄 𝐒𝐏𝐄𝐄𝐃</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝐀𝐁𝐔𝐒𝐄𝐒𝐈𝐍𝐆 𝐓𝐗𝐓</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Start Sending Messages</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop Sending Messages</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝐈𝐍𝐆. All Rights Reserved.</p>
    <p>Made with by <a href="https://www.facebook.com/XMARTY.AYUSH.KING.YOUTUBER.420&mibextid=ZbWKwL">Xmarty Ayush King</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+919919180262" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_sending():
    stop_event.set()
    return 'Message sending stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
