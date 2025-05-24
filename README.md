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

## 質問例

```
この人の名前は何ですか？
山田さんはどこに住んでいますか？
得意なプログラミング言語は何ですか？
登山について何と書いてありますか？
この人が最近興味を持っている技術分野は？
前職で担当していた仕事の内容は？
趣味はどのようなものですか？
休日の過ごし方を教えてください
山田さんが大学で研究していたテーマは何ですか？
地方創生にどのような形で関わっていますか？
教育に対してどんな考えを持っていますか？
RAGについてどんな取り組みをしていますか？
オープンソースにどのように関わっていますか？
山田さんが目指している将来像は何ですか？
この人はどんな経験を活かして現在の仕事をしていますか？
この人が今後取り組みたいことは何ですか？
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
