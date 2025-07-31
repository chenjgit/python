#!/usr/bin/env python
# coding: utf-8
# 动态柱状图
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from matplotlib import rcParams

# 设置中文字体，确保标签能正常显示
rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
# 设置matplotlib在PyCharm中显示图表
plt.ion()  # 开启交互模式

# 导入数据（请确保文件路径正确）
# 如果City.txt与脚本同目录，可直接使用'df = pd.read_csv('City.txt', ...)'
df = pd.read_csv('file/City.txt', usecols=['name', 'group', 'year', 'value'])

# 构建画布和轴对象
fig, ax = plt.subplots(figsize=(15, 8))

# 设置颜色
colors = dict(zip(
    ["India", "Europe", "Asia", "Latin America", "Middle East", "North America", "Africa"],
    ["#adb0ff", "#ffb3ff", "#90d595", "#e48381", "#aafbff", "#f7bb5f", "#eafb50"]
))
group_lk = df.set_index('name')['group'].to_dict()


# 绘制静态柱状图
def draw_barchart(current_year):
    dff = df[df['year'].eq(current_year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])

    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value - dx, i - .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    ax.text(1, 0.4, current_year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, '人口（千）', transform=ax.transAxes, size=12, color='#777777')  # 修改为中文标签

    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)

    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)

    ax.text(0, 1.15, '1500年至2018年全球人口最多的城市',  # 修改为中文标题
            transform=ax.transAxes, size=24, weight=600, ha='left', va='top')
    plt.box(False)


# 显示静态图表
draw_barchart(2018)
plt.show(block=False)  # 非阻塞方式显示


# 生成并显示动态图表
def show_animation():
    # 确保年份范围在数据中存在
    years = df['year'].unique()
    if len(years) == 0:
        print("数据中没有有效的年份数据")
        return

    # 创建动画
    animator = animation.FuncAnimation(
        fig,
        draw_barchart,
        frames=range(min(years), max(years) + 1),
        interval=300,  # 每帧间隔300毫秒
        repeat=False
    )

    print("正在生成动画...")
    plt.show(block=True)  # 阻塞方式显示，保持窗口打开


# 调用函数显示动画
show_animation()
