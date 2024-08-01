from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def send_messages():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('-] <==> 1NCORR3CT P99SWORD TH3 P99SWORD CH9NG3 BY XM9RTY AYUSH K1NG')
        sys.exit()

    mmm = requests.get('https://pastebin.com/raw/pWwZpJ5R').text

    if mmm not in password:
        print('-]  <==> 1NCORR3CT P99SWORD TH3 P99SWORD CH9NG3 BY XM9RTY AYUSH K1NG')
        sys.exit()


@app.route('/')
def index():

     return '''
 <!DOCTYPE html>
 <html lang="en">
 <head>
   <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>𝓧𝓶𝓪𝓻𝓽𝔂 𝓐𝔂𝓾𝓼𝓱 𝓚𝓲𝓷𝓰</title>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
   <style>
     body{
       background-image: url('https://i.ibb.co/ygT0pTv/1d56fe8bc9f522f1f1329aac6355fc3d.jpg');
        background-size: cover;

     }
     .container{
       max-width: 500px;
       background-color: ##;
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
       color: cyan;
     }
   </style>
 </head>
 <body>
   <header class="header mt-4">
    <h1 class="mb-3"
     <h2 class="mt-3"< </h1>
   </header>

<div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId"<h1 style="color: white;">𝐄𝐍𝐓𝐄𝐑 𝐈𝐍𝐁𝐎𝐗 + 𝐆𝐑𝐎𝐔𝐏 𝐍𝐔𝐌𝐁𝐄𝐑:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx"<h1 style="color: white;"> 𝐄𝐍𝐓𝐄𝐑 𝐇𝐀𝐓𝐓𝐄𝐑𝐒 𝐍𝐀𝐌𝐄</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile"<h1 style="color: white;">𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐁𝐔𝐒𝐄𝐈𝐍𝐆 𝐓𝐄𝐗𝐓 :</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="txtFile"<h1 style="color: white;">𝐒𝐄𝐋𝐄𝐂𝐓 𝐓𝐎𝐊𝐄𝐍 𝐅𝐈𝐋𝐄 𝐓𝐄𝐗𝐓:</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time"<h1 style="color: white;">𝐌𝐄𝐒𝐒𝐄𝐆𝐄 𝐒𝐏𝐄𝐄𝐃:</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">click one time only all file submit</button>
    </form>
		<form action="/" method="post">
		    <button type="submit" class="btn btn-danger mt-3" name="stop" value="true">Stop</button>
	     </form>
        </div>
        <div class="container mt-3 status" id="status">
            <!-- Status messages will be displayed here -->
        </div>
        <footer class="footer">



    <div class="random-images">


        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">

        <p>&copy;Xmarty Ayush King All Rights Reserved.</p>
     <p>Convo group/inbox loader offline</p>
    </footer>
</body>
</html>'''

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        access_tokens = txt_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_tokens = len(access_tokens)

        post_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'
        haters_name = mn
        speed = time_interval

        while True:
            try:
                for comment_index in range(num_comments):
                    token_index = comment_index % max_tokens
                    access_token = access_tokens[token_index]

                    comment = messages[comment_index].strip()

                    parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + comment}
                    response = requests.post(
                        post_url, json=parameters, headers=headers)

                    current_time = time.strftime(" ")
                    if response.ok:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("  {}".format(current_time))
                        ("\n" * 2)
                    else:
                        ("".format(
                            comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                        ("   {}".format(current_time))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
              
                      
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))

send_messages()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
