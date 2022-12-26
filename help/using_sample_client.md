# AUTH SERVICE - Using Sample Client

A documentation for using sample client of this service.
English version of this document **is not available**.

このサービスのサンプルクライアントの利用法のドキュメントです。
英語版は**利用できません**。

# I. 前提条件

Python は既にインストールされているものとして、**Python 自体のインストール方法については省略します。**

サンプルクライアントの実行には、以下の条件が必要です。

1. [AUTH SERVICE - Building Environment](https://github.com/fingerpay/auth-service/tree/main/help/building_environment.md) に従って、環境構築が完了していること
2. Python がインストール済であること

# II. 実行

## 1. AUTH SERVICE サーバーの起動

[AUTH SERVICE - Building Environment](https://github.com/fingerpay/auth-service/tree/main/help/building_environment.md) の最後部に記載してある、サーバーの起動方法を参考にして、サーバーを起動します。

## 2. SampleClient の起動

- MacOS または Linux の場合

  以下のコマンドを実行します。

  ```bash
  export port_number=8888
  sh ./client/sample/serve.sh ${port_number}
  ```

- Windows の場合

  以下のコマンドを実行します。

  ```cmd
  cd <このリポジトリのルートパス>\client\sample
  python -m http.server 8888
  ```
  
  なお、ポート番号は変更してもかまいません。

# III. SampleClient の利用

1. 手順 II. が完了したら、ブラウザから [http://localhost:8888/](http://localhost:8888/) にアクセスしてください。
( ポート番号を変更している場合はアドレスのポート番号を変更してください )

2. ブラウザの、「開発者ツール」の、「コンソール」を開いてください。

3. 画面の指示通りログインしてください。

4. コンソールを確認してください。
  ```
  eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk3OGI1NmM2NmVhYmIwZDlhNmJhOGNhMzMwMTU2NGEyMzhlYWZjODciLCJ0eXAiOiJKV1QifQ...
  ```
  のような長い文字列が表示されていれば、成功です。
  この文字列が IDToken となります。
