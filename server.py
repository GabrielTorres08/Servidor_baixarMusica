from flask import Flask, render_template, request, send_from_directory  
from yt_dlp import YoutubeDL
from main import baixar_audio
import os 

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/nome_video", methods=['GET', 'POST'])
def nome_video(key=""):

    if key == "get_url":
        url = request.form.get("url")
        return url

    else:
        url = request.form.get("url")
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

        except Exception as e:
            print("Erro:", e)
            return "Vídeo não encontrado"

        titulo = info.get('title', 'Sem título')
        return render_template("video.html", titulo=titulo, url=url)



@app.route("/download/<path:nome>")
def download(nome):
    pasta = os.path.join(os.getcwd(), "Music")
    return send_from_directory(pasta, nome, as_attachment=True)


@app.route("/baixar")
def baixar():
    url = request.args.get("url")

    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

    except Exception as e:
        print("Erro:", e)
        return "Vídeo não encontrado"

    titulo = info.get('title', 'Sem título')


    baixar_audio(url)


    return render_template('baixar.html', titulo="audio.mp3")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)