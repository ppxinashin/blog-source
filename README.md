# blog-source

热河fen青的 Hugo 博客源码，使用 Blowfish 主题。

## 本地预览

项目使用 Hugo Extended 0.163.3，并通过 Git 子模块管理主题。Blowfish
`v2.104.0` 尚未声明兼容 Hugo 0.164，请保持本地与 CI 版本一致。

```bash
git submodule update --init --recursive
hugo server
```

本地地址为 <http://localhost:1313/>。

## 发布检查

```bash
hugo --gc --minify --panicOnWarning
python3 scripts/check_site.py public
```

推送到 `main` 后，GitHub Actions 会构建站点并发布到
`ppxinashin/ppxinashin.github.io` 的 `main` 分支。
