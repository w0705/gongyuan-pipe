#!/usr/bin/env python3
import os, re

# 所有需要修改的 html 文件
files = ['index.html', 'products.html', 'cases.html', 'about.html', 'contact.html']

for fname in files:
    path = fname
    if not os.path.exists(path):
        print(f'[SKIP] {fname} not found')
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 1. 替换 footer 电话地址
    content = content.replace('电话：400-XXX-XXXX | 地址：XX市XX区XX路XX号', '电话：19933218809 | 地址：河北省邢台市广宗县金园小区 109 商铺')
    # 2. 替换所有页面的 logo 为图片（如果还没改）
    content = content.replace(
        '<div class="logo">\n      <h1>公元管道</h1>\n      <span class="tagline">专业水管·施工改造·值得信赖</span>\n    </div>',
        '<div class="logo">\n      <img src="images/logo.jpg" alt="公元管道" class="logo-img">\n      <span class="tagline">专业水管·施工改造·值得信赖</span>\n    </div>'
    )
    # 3. 去掉 contact.html 的邮箱
    if fname == 'contact.html':
        content = re.sub(r'<div class="info-item">\s*<span class="icon">📧</span>\s*<span>邮箱：info@gongyuan-pipe\.com</span>\s*</div>', '', content)
    # 4. 限制 logo 图片大小
    content = content.replace('src="images/logo.jpg"', 'src="images/logo.jpg" style="max-width:200px; height:auto;"')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'[OK] {fname} updated')

print('All done.')
