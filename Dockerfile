# ベースイメージ
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 必要なPythonライブラリをインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# Flaskアプリケーションを実行
CMD ["python", "app.py"]
