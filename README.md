# Xego Document

<http://xego-dev.basebit.me>

## 运行

安装 [Hugo](https://gohugo.io/getting-started/installing/)。

```sh
# 初次运行的话需要更新 theme
git submodule update --init --recursive

make run
```

open <http://localhost:21313/doc/xego/>

## Fork

fork 后修改以下地方：（把 `xego` 替换为自己的组名）

1. `.gitlab-ci.yml`

   ```yml
   - export TEAM_NAME=xego
   ```

2. `config.toml`

   ```toml
   baseURL = 'http://xego-dev.basebit.me/doc/xego/'
   BookRepo = 'https://git.basebit.me/xego/doc'
   ```

然后就可以在 `./content` 内新建 markdwon 了。

网站会自动发布到 `http://xego-dev.basebit.me/doc/<TEAM_NAME>/` 了。

### Update

```sh
git remote add upstream git@git.basebit.me:xego/doc-template.git
git fetch upstream
git merge upstream/master

# 如果有冲突的话，处理一下冲突

# 以防万一，可以尝试把 theme pull 到最新
cd theme/hugo-book
git checkout master
git pull
cd ../..

# 手动把冲突都处理一下
# 以防万一，可以本地跑一下 make run
make run

# 没啥问题就合并了
```

## 静态文件

[Xego 静态文件](http://xego-dev.basebit.me/doc/xss/2022/05/hugo/#%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6)
