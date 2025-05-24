# Mac上にQwen3 + LlamaIndex を用いたローカルRAG環境を Python で構築する

```
# Python環境セットアップ
$ mise install
$ python --version
Python 3.13.3

# Python仮想環境の構築
$ python -m venv .venv

# Python仮想環境を有効化
$ source .venv/bin/activate

# pipのアップグレード
$ pip install --upgrade pip

$ pip --version
pip 25.1.1

# 必要なライブラリをインストール
$ pip install -r requirements.txt

# 実行
$ python main.py
```

## 仮想環境の再構築

```
$ deactivate
$ rm -rf .venv
$ python -m venv .venv
$ . .venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
