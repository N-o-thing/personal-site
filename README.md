# personal-site

纯静态个人博客，HTML + CSS，部署在 GitHub Pages。

## 项目结构

```
├── index.html         # 首页 — 文章列表
├── about.html         # 关于页面
├── gallery.html       # 图库 + 文件展示
├── style.css          # 全局样式
├── posts/             # 博客文章（.html）
│   └── hello-world.html
├── uploads/
│   ├── images/        # 图片（拖进去就能在图库页展示）
│   └── files/         # 其他文件（供下载）
└── README.md
```

## 写文章

1. 在 `posts/` 里新建一个 `.html` 文件
2. 在 `index.html` 的文章列表里加一条链接
3. 提交并推送，GitHub Pages 自动更新

## 部署

1. GitHub 仓库 Settings → Pages → 选 `main` 分支
2. 等待几分钟，访问 `https://n-o-thing.github.io/personal-site/`
