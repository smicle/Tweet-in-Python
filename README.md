## Tweet-in-Python

### api.yamlを作成

`Twitter API`の情報を記載する。  

```yaml
CLIENT_KEY: "XXXXXXXX"
CLIENT_SECRET: "XXXXXXXX"
RESOURCE_OWNER_KEY: "XXXXXXXX"
RESOURCE_OWNER_SECRET: "XXXXXXXX"
```

### 実行方法

引数にツイート内容を渡す。  
`\n`で改行する事が可能。  

```bash
python ./tweet.py テストツイート
```

### tweet.pyからexeを作成

以下のコマンドを実行する。  

```bash
pyinstaller .\tweet.py --onefile
```

### 参考
[PowerShellからTweetできるコマンドラインツールつくった](https://crimnut.hateblo.jp/entry/2018/04/11/223100)
