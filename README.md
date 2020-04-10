# 沖縄県 新型コロナウイルス感染症対策サイト

東京都版をフォークして作成しています。

[![沖縄県 新型コロナウイルス感染症対策サイト](https://okinawa.stopcovid19.jp/logo.svg)](https://okinawa.stopcovid19.jp)

<!-- ### 日本語 | [English](./docs/en/README.md) | [Español](./docs/es/README.md) | [한국어](./docs/ko/README.md) | [繁體中文](./docs/zh_TW/README.md) | [简体中文](./docs/zh_CN/README.md) | [Tiếng Việt](./docs/vi/README.md) | [ภาษาไทย](./docs/th/README.md) | [Français](./docs/fr/README.md) -->


## 貢献の仕方

Issues にあるいろいろな修正にご協力いただけると嬉しいです。

詳しくは、[貢献の仕方](./CONTRIBUTING.md)を御覧ください。

[沖縄版サイト制作の方針](./PROJECT_OKINAWA.md)のもと、スピード重視で作成されました。  
まだ足りていない機能がたくさんあります。

## 行動原則
詳しくは[サイト構築にあたっての行動原則](./CODE_OF_CONDUCT.md)を御覧ください。

## ライセンス
本ソフトウェアは、[MITライセンス](./LICENSE.txt)の元提供されています。

## 翻訳者向け情報

翻訳をお手伝いいただける方は、[こちらのドキュメント](./TRANSLATION.md)を御覧ください。

## 開発者向け情報

### 環境構築の手順

- 必要となるNode.jsのバージョン: 10.19.0以上

**yarn を使う場合**
```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev
```


**アクセシビリティチェック（vue-axe）を無効にする方法**

- 開発用ローカルサーバが重い場合、以下のようにアクセシビリティチェックを無効にして起動することができます。

```bash
# serve with hot reload at localhost:3000
$ yarn dev-no-axe
```


**docker compose を使う場合**
```bash
# serve with hot reload at localhost:3000
$ docker-compose up --build
```

**Vagrant を使う場合**
```bash
# serve with hot reload at localhost:3000
$ vagrant up
```

### `Cannot find module ****` と怒られた時

**yarn を使う場合**
```bash
$ yarn install
```

**docker compose を使う場合**
```bash
$ docker-compose run --rm app yarn install
```

### VSCode + Remote Containersで開発する場合

1. VSCodeの拡張機能「[Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)」を導入します。
2. [この画像（外部サイト）](https://code.visualstudio.com/docs/remote/containers#_quick-start-try-a-dev-container)のように左下部の「Open Folder in Container」でこのリポジトリのルートを選択すれば環境構築が始まります。

#### Topic
- 設定を変更したい場合は、`.devcontainer/devcontainer.json`を修正してください。
詳細は[devcontainer.jsonのリファレンス](https://code.visualstudio.com/docs/remote/containers#_devcontainerjson-reference)を参照してください。
- Remote Container実行時のみ有効な拡張機能「ESLint」を導入していますが、必要に応じて`devcontainer.json`の`extensions`に追加してください。
詳細な手順は[こちら（外部サイト）](https://code.visualstudio.com/docs/remote/containers#_managing-extensions)を参照してください。
- 開発環境を再構築する場合は、左下部の「Rebuild Container」を実行してください。

### 本番環境/その他の判定

`process.env.GENERATE_ENV` の値が、本番の場合は`'production'`に、それ以外の場合は `'development'` になっています。  
テスト環境のみで実行したい処理がある場合はこちらの値をご利用ください。

### ステージング・本番環境への反映

`master` ブランチがアップデートされると、自動的に `production` ブランチにHTML類がbuildされます。そして、本番サイト https://okinawa.stopcovid19.jp が更新されます。

<!-- `staging` ブランチがアップデートされると、自動的に `gh-pages` ブランチにHTML類がbuildされます。そして、ステージングサイト　https://thirsty-leakey-61fd82.netlify.com/ が更新されます。 -->

`development` ブランチがアップデートされると、自動的に `dev-pages` ブランチにHTML類がbuildされます。そして、開発用サイト https://thirsty-leakey-61fd82.netlify.com/ が更新されます。

### ブランチルール

development以外への Pull Request は禁止です。
Pull Request を送る際の branch は、以下のネーミングルールでお願いします。

機能追加系： feature/#{ISSUE_ID}-#{branch_title_name}  
ホットフィックス系: hotfix/#{ISSUE_ID}-#{branch_title_name}

#### 基本的なブランチ
| 目的 | ブランチ | 確認URL | 備考 |
| ---- | -------- | ---- | ---- |
| 開発 | development | https://thirsty-leakey-61fd82.netlify.com/ | base branch。基本はこちらに Pull Requestを送ってください |
| 緊急適用用 | dev-hotfix | なし | 急ぎ本番に適用するべき修正。管理者から依頼された場合こちらを使ってください |
| ステージング | staging | なし | 本番前の最終確認用。管理者以外の Pull Request は禁止です |
| 本番 | master | https://okinawa.stopcovid19.jp/ | 管理者以外の Pull Request は禁止です |

#### システムで利用しているブランチ
| 目的 | ブランチ | 確認URL | 備考 |
| ---- | -------- | ---- | ---- |
| 本番サイトHTML | production | https://okinawa.stopcovid19.jp/ | 静的ビルドされたHTMLが置いてある場所 |
| ステージングサイト HTML | staging | https://thirsty-leakey-61fd82.netlify.com/ | 静的ビルドされたHTMLが置いてある場所 |
| OGP作業用 | deploy/new_ogp | なし | OGPの更新用 |