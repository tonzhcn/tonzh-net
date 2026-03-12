#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
仝志伟业新闻自动更新系统
每天自动生成 4 篇文章：行业资讯 2 篇 + 技术动态 2 篇
全年无休（365 天）
"""

import json
import os
from datetime import datetime, timedelta
import random

# 配置
NEWS_DIR = "/var/www/tonzh-net/admin"
NEWS_FILE = os.path.join(NEWS_DIR, "news.json")

# 产品关键词库（用于 SEO 优化）
PRODUCT_KEYWORDS = [
    "点胶机", "锡膏印刷机", "贴片机", "回流炉", "波峰焊", "AOI 检测设备",
    "SMT 设备", "表面贴装技术", "电子制造", "半导体设备", "PCB 设备",
    "高精度点胶", "锡膏喷印", "高速贴片", "氮气回流焊", "在线式检测"
]

# 行业关键词
INDUSTRY_KEYWORDS = [
    "5G 通信", "新能源汽车", "智能穿戴", "物联网", "人工智能",
    "工业自动化", "智能制造", "工业 4.0", "中国制造 2025", "半导体产业"
]

# 技术关键词
TECH_KEYWORDS = [
    "工艺优化", "质量控制", "自动化", "精度提升", "效率改善",
    "良率提升", "成本控制", "技术创新", "研发突破", "应用案例"
]

def load_news():
    """加载现有新闻"""
    if os.path.exists(NEWS_FILE):
        with open(NEWS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"articles": []}

def save_news(data):
    """保存新闻数据"""
    os.makedirs(NEWS_DIR, exist_ok=True)
    with open(NEWS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_industry_title():
    """生成行业资讯标题"""
    templates = [
        f"{random.choice(INDUSTRY_KEYWORDS)}领域快速发展，{random.choice(PRODUCT_KEYWORDS)}需求持续增长",
        f"2026 年{random.choice(INDUSTRY_KEYWORDS)}市场趋势分析：{random.choice(PRODUCT_KEYWORDS)}迎来新机遇",
        f"{random.choice(INDUSTRY_KEYWORDS)}产业加速布局，{random.choice(PRODUCT_KEYWORDS)}成关键装备",
        f"政策解读：{random.choice(INDUSTRY_KEYWORDS)}发展规划出台，{random.choice(PRODUCT_KEYWORDS)}受益明显",
        f"{random.choice(INDUSTRY_KEYWORDS)}市场规模突破新高，{random.choice(PRODUCT_KEYWORDS)}国产化率提升",
    ]
    return random.choice(templates)

def generate_tech_title():
    """生成技术动态标题"""
    templates = [
        f"{random.choice(PRODUCT_KEYWORDS)}{random.choice(TECH_KEYWORDS)}方案详解",
        f"如何提升{random.choice(PRODUCT_KEYWORDS)}的{random.choice(TECH_KEYWORDS)}？",
        f"{random.choice(PRODUCT_KEYWORDS)}常见问题分析与{random.choice(TECH_KEYWORDS)}",
        f"创新技术：{random.choice(PRODUCT_KEYWORDS)}实现{random.choice(TECH_KEYWORDS)}",
        f"{random.choice(PRODUCT_KEYWORDS)}工艺优化实践：{random.choice(TECH_KEYWORDS)}案例分享",
    ]
    return random.choice(templates)

def generate_industry_summary(title):
    """生成行业资讯摘要"""
    templates = [
        f"随着{random.choice(INDUSTRY_KEYWORDS)}的快速发展，{random.choice(PRODUCT_KEYWORDS)}市场需求持续增长。本文分析当前市场趋势和发展机遇，为行业提供参考。",
        f"最新数据显示，{random.choice(INDUSTRY_KEYWORDS)}产业规模不断扩大，{random.choice(PRODUCT_KEYWORDS)}作为核心装备，将迎来重要发展机遇。",
        f"在{random.choice(INDUSTRY_KEYWORDS)}政策支持下，{random.choice(PRODUCT_KEYWORDS)}技术创新加速，国产化替代进程明显加快。",
    ]
    return random.choice(templates)

def generate_tech_summary(title):
    """生成技术动态摘要"""
    templates = [
        f"本文详细介绍{random.choice(PRODUCT_KEYWORDS)}的{random.choice(TECH_KEYWORDS)}方案，包括关键技术要点、实施步骤和注意事项，为工程师提供参考。",
        f"针对{random.choice(PRODUCT_KEYWORDS)}应用中的常见问题，本文提供系统的{random.choice(TECH_KEYWORDS)}方法，帮助提升生产效率和产品质量。",
        f"通过实际案例分析，分享{random.choice(PRODUCT_KEYWORDS)}在{random.choice(TECH_KEYWORDS)}方面的成功经验，包括参数设置、工艺优化等关键内容。",
    ]
    return random.choice(templates)

def generate_content(summary, product_links=None):
    """生成文章内容（简化版，实际可调用 AI API）"""
    content = f"""
    <article>
        <section>
            <h2>行业背景</h2>
            <p>{summary}</p>
            <p>随着电子制造行业的快速发展，SMT 设备作为核心装备，其技术水平和性能指标直接影响生产效率和产品质量。</p>
        </section>
        
        <section>
            <h2>技术要点</h2>
            <p>在现代电子制造中，{random.choice(PRODUCT_KEYWORDS)}的应用越来越广泛。选择合适的设备需要综合考虑以下因素：</p>
            <ul>
                <li>设备精度和稳定性</li>
                <li>生产效率和产能</li>
                <li>操作便捷性和维护成本</li>
                <li>技术支持和售后服务</li>
            </ul>
        </section>
        
        <section>
            <h2>应用案例</h2>
            <p>某知名电子制造企业通过引入先进的{random.choice(PRODUCT_KEYWORDS)}，成功实现了生产效率提升 30%，产品良率提高 15% 的显著效果。</p>
        </section>
        
        <section>
            <h2>未来展望</h2>
            <p>随着{random.choice(INDUSTRY_KEYWORDS)}的持续发展，{random.choice(PRODUCT_KEYWORDS)}将朝着更高精度、更高效率、更智能化的方向演进。</p>
        </section>
        
        <section>
            <h2>相关产品</h2>
            <p>仝志伟业提供完整的 SMT 设备解决方案，包括：</p>
            <ul>
                <li><a href="/products/dispenser/">点胶机系列</a> - 高精度点胶设备</li>
                <li><a href="/products/solder-printer/">锡膏印刷机系列</a> - 精密印刷解决方案</li>
                <li><a href="/products/placer/">贴片机系列</a> - 高速高精度贴装</li>
                <li><a href="/products/desktop-reflow/">回流炉系列</a> - 多种焊接工艺</li>
                <li><a href="/products/aoi/">AOI 检测设备</a> - 自动光学检测</li>
            </ul>
        </section>
    </article>
    """
    return content.strip()

def create_news_article(category, date):
    """创建单篇新闻文章"""
    if category == "行业资讯":
        title = generate_industry_title()
        summary = generate_industry_summary(title)
    else:  # 技术动态
        title = generate_tech_title()
        summary = generate_tech_summary(title)
    
    # 生成文章 ID
    article_id = date.strftime("%Y%m%d") + "-" + category[:2] + "-" + str(random.randint(100, 999))
    
    # 生成文章链接
    category_dir = "industry" if category == "行业资讯" else "technology"
    link = f"/news/{category_dir}/{article_id}.html"
    
    return {
        "id": article_id,
        "title": title,
        "date": date.strftime("%Y-%m-%d"),
        "category": category,
        "summary": summary,
        "content": generate_content(summary),
        "link": link,
        "author": "仝志伟业",
        "views": 0,
        "tags": [random.choice(PRODUCT_KEYWORDS), random.choice(TECH_KEYWORDS)]
    }

def update_news():
    """执行新闻更新"""
    print(f"[{datetime.now()}] 开始更新新闻...")
    
    data = load_news()
    today = datetime.now()
    
    # 检查今天是否已更新
    today_str = today.strftime("%Y-%m-%d")
    existing_today = [a for a in data["articles"] if a["date"] == today_str]
    
    if len(existing_today) >= 4:
        print(f"今天已更新{len(existing_today)}篇文章，无需重复更新")
        return
    
    # 生成今日新闻：行业资讯 2 篇 + 技术动态 2 篇
    new_articles = []
    
    # 行业资讯 2 篇
    for i in range(2):
        article = create_news_article("行业资讯", today)
        article["title"] = f"[{i+1}] {article['title']}"
        new_articles.append(article)
        print(f"✓ 生成行业资讯：{article['title'][:50]}...")
    
    # 技术动态 2 篇
    for i in range(2):
        article = create_news_article("技术动态", today)
        article["title"] = f"[{i+1}] {article['title']}"
        new_articles.append(article)
        print(f"✓ 生成技术动态：{article['title'][:50]}...")
    
    # 添加到新闻列表（最新的在前）
    data["articles"] = new_articles + data["articles"]
    
    # 保存
    save_news(data)
    
    print(f"[{datetime.now()}] 更新完成，共生成{len(new_articles)}篇文章")
    print(f"当前新闻总数：{len(data['articles'])}篇")

if __name__ == "__main__":
    update_news()
