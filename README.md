# Misskey Anniversary Bot

このアプリケーションは、設定した日付から記念日を計算し、任意のMisskeyサーバーへ投稿するBotです。

## アプリケーションの概要

以下の条件に合致するとき、投稿を行います。

- 100n日
- ゾロ目の日
- n周年
- n.5周年

また、投稿の文言は以下の部分を編集してください。

```python:main.py
if last_note != dt_now:
    if anniversaries:
        for anniversary in anniversaries:
            note_text = f"#ここを編集"
            mk.notes_create(text=note_text)
            last_note = dt_now
```

## セットアップ

アプリケーションをローカルで実行するために、以下の手順に従ってください。

1. このリポジトリをクローンします。

   ```bash
   git clone https://github.com/Soli0222/mk-anniv.git
   ```

2. 環境変数を設定します。

   ```bash
   cp .env.example .env
   ```

    ``.env``ファイルを開き、内容を編集します。

   ```.env
   MISSKEY_SERVER=サーバーのURL (2つ目の@以下)
   API_TOKEN=APIトークン
   SETUP_YEAR=年
   SETUP_MONTH=月
   SETUP_DAYS=日
   ```

3. 必要なモジュールをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

## 実行

```bash
python main.py
```
