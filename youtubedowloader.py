# import yt_dlp
# from flask import Flask, request, render_template_string
# import webbrowser
# import threading
# import os

# output_path = r"E:\Youtube Videos Download"
# app = Flask(__name__)

# def open_browser():
#     webbrowser.open("http://localhost:5000")

# @app.route('/', methods=['GET', 'POST'])
# def download_video():
#     if request.method == 'POST':
#         video_url = request.form['url']

#         # Validate the YouTube URL format
#         if "youtube.com/watch" not in video_url and "youtu.be" not in video_url:
#             return "Invalid YouTube URL. Please enter a valid video link."
        
#         try:
#             # Set yt-dlp options
#             ydl_opts = {
#                 'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Ensure path format
#                 'format': 'best',  # Download the best format available
#             }

#             # Download the video
#             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#                 ydl.download([video_url])

#             # Check if the file exists in the output directory
#             downloaded_files = os.listdir(output_path)
#             return f"Download complete! Files in {output_path}: {downloaded_files}"

#         except Exception as e:
#             return f"An error occurred: {e}"

#     return render_template_string('''
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>YouTube Video Downloader</title>
#             <style>
#                 body {
#                     font-family: Arial, sans-serif;
#                     margin: 0;
#                     padding: 0;
#                     height: 100vh;
#                     background: linear-gradient(45deg, #ff6ec7, #f7b7a3);
#                     background-size: 400% 400%;
#                     animation: gradientAnimation 15s ease infinite;
#                     display: flex;
#                     justify-content: center;
#                     align-items: center;
#                     text-align: center;
#                     color: white;
#                 }

#                 @keyframes gradientAnimation {
#                     0% { background-position: 0% 50%; }
#                     50% { background-position: 100% 50%; }
#                     100% { background-position: 0% 50%; }
#                 }

#                 form {
#                     background-color: rgba(0, 0, 0, 0.5);
#                     padding: 20px;
#                     border-radius: 10px;
#                     width: 300px;
#                     box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.7);
#                 }

#                 input[type="text"] {
#                     padding: 10px;
#                     margin: 10px 0;
#                     width: 100%;
#                     border-radius: 5px;
#                     border: none;
#                     font-size: 16px;
#                 }

#                 input[type="submit"] {
#                     padding: 10px 20px;
#                     background-color: #ff6ec7;
#                     color: white;
#                     border: none;
#                     border-radius: 5px;
#                     cursor: pointer;
#                     font-size: 16px;
#                     width: 100%;
#                 }

#                 input[type="submit"]:hover {
#                     background-color: #f7b7a3;
#                 }

#                 .message {
#                     margin-top: 40px;
#                     margin-left: 20px;
#                     font-size: 18px;
#                     color: #fff;
#                 }

#             </style>
#         </head>
#         <body>
#             <form method="post">
#                 <h1>YouTube Video Downloader</h1>
#                 <label for="url">Video URL:</label>
#                 <input type="text" name="url" id="url" required>
#                 <input type="submit" value="Download">
#             </form>
#             <div class="message">
#                 {{ message }}
#             </div>
#         </body>
#         </html>
#     ''', message="Please enter a video URL to download.")

# if __name__ == '__main__':
#     # Open the browser after starting the server
#     threading.Timer(1, open_browser).start()
#     app.run(debug=True)

import yt_dlp
from flask import Flask, request, render_template_string
import webbrowser
import threading
import os

# Set the output directory for downloaded files
output_path = r"E:\Web Programming"

# Initialize the Flask app
app = Flask(__name__)

# Automatically open the browser
def open_browser():
    webbrowser.open("http://localhost:5000")

# HTML Template for the downloader
template = '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Downloader</title>
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
            font-size: 18px;
            color: #fff;
        }
    </style>
</head>
<body>
    <form method="post">
        <h1>YouTube Video Downloader</h1>
        <label for="url">Video URL:</label>
        <input type="text" name="url" id="url" required>
        <input type="submit" value="Download">
    </form>
    <div class="message">
        {{ message }}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def download_video():
    # Default message for the webpage
    message = "Enter a video URL to download."

    if request.method == 'POST':
        video_url = request.form['url']

        # Validate the YouTube URL format
        if "youtube.com/watch" not in video_url and "youtu.be" not in video_url:
            message = "Invalid YouTube URL. Please try again."
        else:
            try:
                # Set yt-dlp options
                ydl_opts = {
                    'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save files in the specified directory
                    'format': 'best',  # Best video/audio format
                }

                # Download the video
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

                # Success message
                message = "Download complete! Ready for the next one."

            except Exception as e:
                # Log the error and show a user-friendly message
                print(f"Error: {e}")
                message = "An unexpected error occurred. Please try again."

    # Render the template with the updated message
    return render_template_string(template, message=message)

if __name__ == '__main__':
    # Automatically open the browser and start the Flask app
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
