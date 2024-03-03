# gemtext

a python library and CLI tool for parsing gemtext and converting it to various targets.

[about](https://geminiprotocol.net/docs/gemtext.gmi)

this readme file was written in gemtext and converted to markdown via this library, by running the below command:

```sh
python -m gemtext readme.gmi > README.md
```

## supported targets

- html
- markdown

## how it works

- gemtext is parsed into an abstract syntax tree
- the abstract syntax tree is "rendered" to the target format

## goals

- follow the gemtext spec and conventions as accurately and completely as possible.
- convert to targets as un-opinionatedly as possible
- sane errors/warnings


