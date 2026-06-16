# 小站 · personal-site

记录一些想法和折腾的东西。

👉 **https://n-o-thing.github.io/personal-site/**

---

## 这是什么

纯静态个人博客，HTML + CSS，部署在 GitHub Pages。

每篇文章是一个 `.html` 文件，push 到 GitHub 后自动部署上线。

## 项目结构

```
├── index.html         # 首页 — 文章列表
├── about.html         # 关于
├── gallery.html       # 图库 + 文件下载
├── style.css          # 样式
├── posts/             # 博客文章
│   └── hello-world.html
├── uploads/
│   ├── images/        # 图片
│   └── files/         # 其他文件
├── .nojekyll          # 关闭 Jekyll，纯静态直发
└── README.md
```

## License

MIT
