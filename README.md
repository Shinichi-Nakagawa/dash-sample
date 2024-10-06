# 実践Dashのsample code

[実践Dash - 手を抜きながら本気で作るデータApplicationの基本と応用](https://speakerdeck.com/shinyorke/dash-for-python-and-baseball)のスライド内に登場したサンプルとちょっとした補足.

## Setting

### lib install

#### pip

```bash
pip install -r requirements.txt
```

#### poetry

```bash
poetry install
```

### Data

[Sean Lahman Baseball DataのBatting.csv](https://www.dropbox.com/scl/fi/hy0sxw6gaai7ghemrshi8/lahman_1871-2023_csv.7z?e=1&file_subpath=%2Flahman_1871-2023_csv&rlkey=edw1u63zzxg48gvpcmr3qpnhz&st=fafzoub1&dl=0)を使います.

上記Dropboxからアーカイブをダウンロードして`Batting.csv`を入手し利用してください.

### 実行

すべてのアプリケーションは`Batting.csv`を配置（`app.py`と同じ階層にあること）してディレクトリを移動後, 以下のコマンドを実行.

```bash
python app.py
```

Debugモードなので, `http://127.0.0.1:8050/` を開くと表示.

また, gunicornでの起動も可能.

```bash
gunicorn app:server
```

`http://127.0.0.1:8000/` を開くと表示（Portが異なるので注意）.

## sample code

### Hello world

最もシンプルなページ

[/01_simple_app/](./01_simple_app/)

### 認証認可

Basic Authによるシンプルな認証

[/02_auth/](./02_auth/)

### マルチページ

複数ページでのアプリケーション

[/03_multipage/](./03_multipage/)

## License

[MIT License](./LICENSE)