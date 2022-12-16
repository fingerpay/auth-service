# AUTH SERVICE - Developing Clients

A documentation for developing clients.
English version of this document **is not available**.

このサービスのクライアント ( フロントエンド ) を開発するためのドキュメントです。
英語版は**利用できません**。

# I. 全景の説明

ここでいう、「認証」とは、**Google アカウントでログインしていることを Firebase に証明してもらう**ことのみを指しています。

## 1. システムコンポーネント

このサービスは、主に次の 2 つのサーバーによって実現されています。

1. Firebase Authentication

   Google が提供する、認証提供サービスです。

   Firebase は、ユーザーの `idToken` を取得する目的でのみ用います。

   ( Firebase はユーザー認証のみを行い、**ユーザー情報の保存は行わいない**。 )

2. auth-service サーバー

   このサーバーです。
   
   **Firebase から渡された idToken を基に、**ユーザー情報の保存を行います。
   
   このサーバーが、ユーザーの情報などを保存します。

## 2. システム関係図

このシステムは、 [【FastAPI+Firebase】Bearer認証を行うAPIサーバの構築 - Qiita](https://qiita.com/Seo-4d696b75/items/6fc3792d034c2a01b830) を参考にして構築されています。

それぞれの関係図は、以下のとおりです。

![system-image](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F440643%2F54b6ef41-f2bf-9722-0f42-9982a9c35605.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=d05a1f389d9ac6c455b6efed9f78aa26)

# II. 実装

## 1. 具体的な認証フロー

クライアントが以下の手順を踏むことで、認証が行われます。

1. クライアントのブラウザから Firebase の認証画面にアクセスし、任意のログイン方法でログインする。 ( 画像 ① )
2. クライアントのブラウザから Firebase の idToken を発行する。 ( 画像 ① )
3. idToken を `authorization: Bearer` ヘッダーにセットして、AUTH SERVICE へアクセスする。 ( 画像 ② )
4. ユーザーが認証される。 ( 画像 ④ )

## 2. AUTH SERVICE へのアクセス

このサービスのエンドポイントにアクセスする際は、必ず次のヘッダーを付与してリクエストしてください。

```
authorization: Bearer <Firebase から取得した idToken >
```

具体例:
```
authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImE5NmFkY2U5OTk5YmJmNWNkMzBmMjlmNDljZDM3ZjRjNWU2NDI3NDAiLCJ0eXAiOiJKV1QifQ...
```

**Client が認証に必要なことは、Firebase から idToken を取得して、AUTH SERVICE に転送するだけです。**

## 3. Client の実装例

### a. Sample Client

`client/sample` の実装を参考にしてください。

Sample Client の使用方法は、[AUTH SERVICE - Building Environment](https://github.com/fingerpay/auth-service/tree/main/help/using_sample_client.md) を参照してください。

### b. 具体的な実装例 ( JS )

詳しくは、Google 公式から提供されているリファレンスを参照してください。

[auth package  |  Firebase JavaScript API reference](https://firebase.google.com/docs/reference/js/auth.md#auth_package)

ログイン

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Firebase Auth for Google</title>
    <link type="text/css" rel="stylesheet" href="https://cdn.firebase.com/libs/firebaseui/3.5.2/firebaseui.css"/>
    <style>h1 {
        text-align: center;
    }</style>
</head>
<body>
<h1>Firebase Auth for Google</h1>
<div id="firebaseui-auth-container"></div>

<!-- Loads Firebase Library -->
<!-- Firebase ライブラリの読み込み -->
<script src="https://www.gstatic.com/firebasejs/5.8.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.8.1/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/ui/3.5.2/firebase-ui-auth__ja.js"></script>

<!-- Loads and initializes a Firebase app -->
<!-- Firebase app の読み込みと初期化 -->
<script src="/config.js"></script>

<script>
    //----------------------------------------------
    // Firebase UIの設定
    //----------------------------------------------
    var uiConfig = {
        // ログイン完了時のリダイレクト先
        signInSuccessUrl: '/done.html',

        // 利用する認証機能 ( Google アカウントのみ )
        signInOptions: [
            firebase.auth.GoogleAuthProvider.PROVIDER_ID
        ],
    };

    var ui = new firebaseui.auth.AuthUI(firebase.auth());
    ui.start('#firebaseui-auth-container', uiConfig);
</script>
</body>
</html>
```

tokenID を取得する

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Firebase Auth for Google</title>
</head>
<body>
<h1>...Please wait</h1>
<div id="info"></div>

<!-- Loads Firebase Library -->
<!-- Firebase ライブラリの読み込み -->
<script src="https://www.gstatic.com/firebasejs/5.8.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.8.1/firebase-auth.js"></script>

<!-- Loads and initializes a Firebase app -->
<!-- Firebase app の読み込みと初期化 -->
<script src="/config.js"></script>

<script>
    firebase.auth().onAuthStateChanged((user) => {
        let h1 = document.querySelector('h1');
        let info = document.querySelector('#info');

        // Call firebase.auth().currentUser.getIdToken() to receive JWT token
        // user.getIdToken() can be used too
        // firebase.auth().currentUser.getIdToken() を呼び出して JWT トークンを受け取り
        //user.getIdToken() でも同じ結果を得られます
        firebase.auth().currentUser.getIdToken(/* forceRefresh */ true).then(function (idToken) {
            console.log("DANGER!!!");
            console.log("The following string is used to IT'S YOU!");
            console.log("So, keep secret the following string:")
            console.log(idToken);
        })

        if (user) {
            h1.innerText = 'Sign In Complete!';
            info.innerHTML = `Signed in as ${user.displayName}<br>` +
                `(UID: ${user.uid}}<br>`;
        } else {
            h1.innerText = 'Not Signed In';
        }
    });
</script>
</body>
</html>
```
