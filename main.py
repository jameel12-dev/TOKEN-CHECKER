from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

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

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XM9RTY AYUSH K1NG</title>
    <style>
        .header {
            display: flex;
            align-items: center;
        }
        .header h1 {
            margin: 0 20px;
        }
        .header img {
            max-width: 100px; 
            margin-right: 20px;
        }
        .random-img {
            max-width: 300px;
            margin: 10px;
        }
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <h1 class="mb-3" style="color: blue;">AYUSH MULTI COOKIE POST SERVER</h1>
        <h1 class="mt-3" style="color: red;"> (RAPPIIEST)</h1>
    </header>
<div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
            <label for="threadId">POST ID:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
            <label for="kidx">Enter Hater Name:</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
            <label for="messagesFile">Select Your Np File:</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="cookiesFile">Select Your Cookies File:</label>
            <input type="file" class="form-control" id="cookiesFile" name="cookiesFile" accept=".txt" required>
        </div>
        <div class="mb-3">
            <label for="time">Speed in Seconds (minimum 60 second):</label>
            <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
    </form>
</div>
    <div class="random-images">
    </div>
    <footer class="footer">
        <p style="color: #FF5733;">Post Loader Tool</p>
        <p>Made with by rohit<a </a></p>
    </footer>
</body>
</html>'''

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        cookies_file = request.files['cookiesFile']
        cookies_data = cookies_file.read().decode().splitlines()

        messages_file = request.files['messagesFile']
        messages = messages_file.read().decode().splitlines()

        num_comments = len(messages)
        max_cookies = len(cookies_data)

        post_url = f'https://graph.facebook.com/v15.0/{thread_id}/comments'
        haters_name = mn
        speed = time_interval

        session = requests.Session()

        while True:
            try:
                for comment_index in range(num_comments):
                    cookie_index = comment_index % max_cookies
                    cookie_string = cookies_data[cookie_index]

                    # Parsing cookies
                    cookies = {}
                    for cookie in cookie_string.split(';'):
                        key, value = cookie.strip().split('=', 1)
                        cookies[key] = value

                    comment = messages[comment_index].strip()

                    parameters = {'message': haters_name + ' ' + comment}
                    response = session.post(
                        post_url, data=parameters, cookies=cookies, headers=headers)

                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    if response.ok:
                        print("[+] Comment No. {} Post Id {} Cookie No. {}: {}".format(
                            comment_index + 1, post_url, cookie_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("\n" * 2)
                    else:
                        print("[x] Failed to send Comment No. {} Post Id {} Cookie No. {}: {}".format(
                            comment_index + 1, post_url, cookie_index + 1, haters_name + ' ' + comment))
                        print("  - Time: {}".format(current_time))
                        print("  - Status Code: {}".format(response.status_code))
                        print("  - Response: {}".format(response.text))
                        print("\n" * 2)
                    time.sleep(speed)
            except Exception as e:
                print(e)
                time.sleep(30)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
