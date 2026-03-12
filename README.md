# 北京仝志伟业 - SMT 设备官网

**域名**：tonzh.net  
**定位**：专业 SMT 设备供应商  
**公司**：北京仝志伟业公司

---

## 网站结构

```
tonzh-net/
├── index.html              # 首页
├── about/
│   └── index.html          # 关于我们
├── products/
│   ├── index.html          # 产品中心
│   ├── dispenser/          # 点胶机系列
│   ├── solder-printer/     # 锡膏印刷机系列
│   ├── solder-jetter/      # 锡膏喷印机系列
│   ├── placer/             # 贴片机系列
│   ├── loose-parts-placer/ # 散料贴片机系列
│   ├── desktop-reflow/     # 台式回流炉系列
│   ├── nitrogen-reflow/    # 氮气回流炉系列
│   ├── inline-reflow/      # 在线式回流炉系列
│   ├── wave-soldering/     # 波峰焊系列
│   ├── aoi/                # AOI 检测设备系列
│   └── auxiliary/          # 辅助设备系列
├── news/
│   └── index.html          # 新闻动态
├── contact/
│   └── index.html          # 联系我们
├── css/
│   └── style.css           # 样式文件
├── js/
│   └── main.js             # 脚本文件
└── images/                 # 图片资源
```

---

## 产品类别（11 个）

1. **点胶机系列** - 高精度点胶设备
2. **锡膏印刷机系列** - 精密锡膏印刷
3. **锡膏喷印机系列** - 非接触式喷印
4. **贴片机系列** - 高速高精度贴装
5. **散料贴片机系列** - 散料元器件贴装
6. **台式回流炉系列** - 紧凑型回流焊接
7. **氮气回流炉系列** - 惰性气体保护焊接
8. **在线式回流炉系列** - 全自动在线焊接
9. **波峰焊系列** - 通孔元器件焊接
10. **AOI 检测设备系列** - 自动光学检测
11. **辅助设备系列** - SMT 周边设备

---

## 部署说明

### 本地测试
```bash
cd /home/admin/.openclaw/workspace/tonzh-net
python3 -m http.server 8000
# 访问 http://localhost:8000
```

### 部署到服务器
```bash
# 推送到 GitHub
git add -A
git commit -m "提交信息"
git push origin main

# 或使用 Vercel 部署
vercel --prod
```

---

## 待办事项

- [ ] 补充公司介绍详细内容
- [ ] 添加产品图片
- [ ] 完善各产品详情页技术参数
- [ ] 添加联系方式（电话、邮箱、地址）
- [ ] 新闻动态页面开发
- [ ] 联系表单后端集成
- [ ] SEO 优化（keywords、sitemap）
- [ ] 网站备案（如需要）

---

**创建时间**：2026-03-12  
**版本**：v1.0
