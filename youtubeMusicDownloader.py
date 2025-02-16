import yt_dlp
from flask import Flask, request, render_template_string
import webbrowser
import threading
import os

# Set the output directory for downloaded files
output_path = r"E:\Youtube Music Download"

# Initialize the Flask app
app = Flask(__name__)

# Open the browser automatically
def open_browser():
    webbrowser.open("http://localhost:5000")

# HTML Template for the downloader
template = '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Music Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            background: linear-gradient(45deg, #ff6ec7, #f7b7a3);
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }
        @keyframes gradientAnimation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        form {
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            width: 300px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.7);
        }
        input[type="text"] {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #ff6ec7;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #f7b7a3;
        }
        .message {
            margin-top: 40px;
            margin-left: 20px;
            font-size: 18px;
            color: #fff;
        }
    </style>
</head>
<body>
    <form method="post">
        <h1>YouTube Music Downloader</h1>
        <label for="url">Video URL:</label>
        <input type="text" name="url" id="url" required>
        <input type="submit" value="Download as MP3">
    </form>
    <div class="message">
        {{ message }}
        <p>Check your downloads here: <a href="file://{{ output_path }}" target="_blank">{{ output_path }}</a></p>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        video_url = request.form['url']
        if "youtube.com/watch" not in video_url and "youtu.be" not in video_url:
            return render_template_string(template, message="Invalid YouTube URL. Please try again.", output_path=output_path)
        try:
            ydl_opts = {
                'outtmpl': os.path.join(output_path, '%(title)s_%(id)s.%(ext)s'),
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return render_template_string(template, message="Download complete! Ready for the next one.", output_path=output_path)
        except Exception:
            # Log the error and show a generic message
            print("An error occurred while downloading the video.")
            return render_template_string(template, message="An unexpected error occurred. Please try again.", output_path=output_path)
    return render_template_string(template, message="Enter a video URL to download.", output_path=output_path)

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
