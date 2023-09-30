from flask import Flask,render_template,request
import base64
import os
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_photo", methods=['POST'])
def upload_photo():
    # OnClickVideoで画像を撮影する
    photo_data = request.json['photo']
    # 写真データをデコードして保存
    save_photo(photo_data, 'static/photos', 'snapshot.png')
    # 保存した写真を表示
    return render_template("index.html")

def save_photo(photo_data, save_dir, file_name):
    # base64エンコードされた写真データをデコード
    photo_bytes = base64.b64decode(photo_data.split(',')[1])

    # ファイルの保存先ディレクトリを作成
    os.makedirs(save_dir, exist_ok=True)

    # ファイルパスを結合
    file_path = os.path.join(save_dir, file_name)

    # 写真をファイルとして保存
    with open(file_path, 'wb') as f:
        f.write(photo_bytes)