# AUTH SERVICE - Building Environment

A documentation for building the environment of this service.
English version of this document **is not available**.

このサービスの環境を構築するためのドキュメントです。
英語版は**利用できません**。

# I. Firebase

このサービスは、Firebase を利用しています。
まずはじめに、Firebase のプロジェクトを作成してください。

## 1. プロジェクトを作成する

**本番環境の場合、既にプロジェクトを作成済みの場合は、不要な手順です。**

[[Firebase初学者向け] Firebaseのはじめかた – 新規で「プロジェクトA」を作ってみよう | DevelopersIO](https://dev.classmethod.jp/articles/firebase-project-get-started/) を参考にして、プロジェクトを作成してください。

記事中の、**「ユーザを追加する」の手順は不要です。**

## 2. 秘密鍵 をダウンロードする

Firebase にアクセスするために必要な認証情報をダウンロードします。

[Firebase Admin SDK で Firebase の各種サービスを操作する｜まくろぐ](https://maku.blog/p/yfov4bi/) を参考にして、秘密鍵をダウンロードします。

記事中の、**「Node.js (TypeScript) プロジェクトの作成」以降の手順はすべて不要です。**

```bash
./secrets/myapp-12345-firebase-adminsdk-xxxxx.json
```

ダウンロードしたファイルを上のパスに配置し、その**ファイルへのパスを控えておいてください**。

## 3. Firebase App を作成する ( Client を開発、使用する場合のみ )

クライアントが Firebase にアクセスするための Config を生成する手順です。

**クライアント (フロントエンド) を開発する場合のみに必要な手順です。**

1. [Firebase の Console](https://console.firebase.google.com/)にログインします。
2. 手順 1. で作成したプロジェクトを選択します。
3. 画面左上の ⚙ ( 歯車マーク ) をクリックします。
4. "Project Settings" をクリックします。
5. "General" が青色になって選択されていることを確認します。
6. "Your apps" のところの、"Add app" というボタンをクリックします。
7. Web ( `</>` のアイコン ) をクリックします。
8. "App nickname" に、任意の名前を入力します。
9. "Register App" ボタンをクリックします。
10. "Use a \<script\> tag" を選択します。
11. 表示された文字列をコピーします。

以上の手順を終えると、以下のような文章が表示されるはずです。

```js
<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  const firebaseConfig = {
    apiKey: "XXXXXXXXXXXXX",
    authDomain: "XXXXXXXXXXXXX",
    projectId: "XXXXXXXXXXXXX",
    storageBucket: "XXXXXXXXXXXXX",
    messagingSenderId: "XXXXXXXXXXXXX",
    appId: "XXXXXXXXXXXXX"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
</script>
```

このうち、

```js
const firebaseConfig = {
  apiKey: "XXXXXXXXXXXXX",
  authDomain: "XXXXXXXXXXXXX",
  projectId: "XXXXXXXXXXXXX",
  storageBucket: "XXXXXXXXXXXXX",
  messagingSenderId: "XXXXXXXXXXXXX",
  appId: "XXXXXXXXXXXXX"
};
```

の部分のみをコピーし、

`./client/sample/pages/config.js` の

```js
const firebaseConfig = {
    apiKey: "AIzaSyDF32SRWapOxiQp32GN4u7x38E_GT0mX5o",
    authDomain: "colk-test-a3fad.firebaseapp.com",
    projectId: "colk-test-a3fad",
    storageBucket: "colk-test-a3fad.appspot.com",
    messagingSenderId: "166004881492",
    appId: "1:166004881492:web:cead296411300befb1d5c1"
};
```

**の部分のみに貼り付けます。**

なお、**最後の行に**

```js
firebase.initializeApp(firebaseConfig);
```

**と書かれていることを必ず確認してください。**

# II. Python / Poetry のセットアップ

このサービスのサーバー自体は、Python にて記述されています。

Python は既にインストールされているものとして、**Python 自体のインストール方法については省略します。**

## 1. Poetry のインストール

[Poetry documentation (ver. 1.1.6 日本語訳)](https://cocoatomo.github.io/poetry-ja/) を参考にして、Poetry をインストールしてください。

## 2. パッケージのインストール

以下のコマンドを実行して、パッケージをインストールします。

```bash
poetry install
```

# III. Docker / DockerCompose のセットアップ

ここでは省略します。
必要に応じてセットアップしてください。

# IV. 環境変数の設定

以下の環境変数を、OS に設定してください。

以下は UNIX 系の場合です。
Windows の場合は、適するように読み替えてください。

必要に応じて .env などを活用してもよいでしょう。

```bash
# 任意の変数
# 1 でデバッグモードデバッグモードをオンにする。
export FP_AUTH_IS_DEBUG="1"

# 必須の変数
# 問い合わせ先の PostgreSQL のホスト
export FP_AUTH_POSTGRES_HOST="172.16.238.20"
# 問い合わせ先の PostgreSQL のポート
export FP_AUTH_POSTGRES_PORT="5432"
# 問い合わせ先の PostgreSQL のユーザー名
export FP_AUTH_POSTGRES_USER_NAME="fingerpay"
# 問い合わせ先の PostgreSQL のパスワード
export FP_AUTH_POSTGRES_PASSWORD="password"
# 問い合わせ先の PostgreSQL のデータベース名
export FP_AUTH_POSTGRES_DB_NAME="fingerpay_auth"

# 必須の変数
# 利用する Firebase の秘密鍵へのパス
export FP_AUTH_FIREBASE_KEY_PATH="/Users/colk/Repositories/fingerpay/auth-service/secrets/account_key.json"
```

# V. 起動

以下のコマンドで起動できます。

```bash
poetry shell
export port_number=8080
uvicorn api.main:app --port ${port_number} --reload
```

なお、`port_number` の値は変更しても構いません。
