# 薄膜应变片计算工具包

一个基于Python的应变片参数计算工具包，包含核心计算模块和用户友好的Web界面。

[简体中文](README/README_zh.md) | [English](README.md)

## 概述

本工具包提供薄膜应变片关键参数的计算功能，如应变系数、微应变和灵敏系数（GF）。主要包括：
- 核心计算模块（`basic_calculation.py`），包含基本的应变片计算公式
- 交互式Web界面，支持参数输入和实时计算

## 功能特点

- **核心计算**：利用应变片的基本力学和电学特性，计算与应变成相关的参数
- **Web界面**：易于使用的浏览器界面，支持输入验证和单位转换（Ω、kΩ、MΩ）
- **交互式结果**：实时计算以下参数：
  - 应变系数（epsilon）
  - 微应变（μ_epsilon）
  - 灵敏系数（GF）

## 安装

### 前提条件
- Python 3.7及以上版本
- pip（Python包管理器）

### 步骤
1. 克隆仓库：
   ```bash
   git clone https://github.com/your-username/foil-strain-gauge-calculation-toolkit.git
   cd foil-strain-gauge-calculation-toolkit
   ```

2. 安装所需依赖（若不存在`requirements.txt`，请创建并包含Flask等必要包）：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 1. 使用核心计算模块
在Python脚本中导入`basic_calculation`模块，直接使用计算函数：
```python
from code.basic_calculation import epsilon_calculate
from code.basic_calculation import gf_sensitivity_calculate

# 使用示例
params = {
    "y": 0.5,    # 自由端挠度（mm）
    "x": 20,     # 应变片到加载点的距离（mm）
    "h": 3,      # 梁厚度（mm）
    "l": 100,    # 悬臂梁长度（mm）
    "R0": 120,   # 零应变电阻（Ω）
    "R1": 120.1  # 当前电阻（Ω）
}

epsilon_calculate = epsilon_calculate(**params)
gf_sensitivity_calculate = gf_sensitivity_calculate(**params)

print(f"应变系数：{epsilon_calculate['epsilon']}")
print(f"微应变：{epsilon_calculate['mu_epsilon']}")
print(f"灵敏系数：{gf_sensitivity_calculate['gf']}")
```

### 2. 使用Web界面
1. 启动Web应用：
   ```bash
   python web/basic_calculation/app.py
   ```

2. 打开浏览器，访问`http://localhost:5000`（或输出中指定的端口）

3. 输入所需参数：
   - 自由端挠度（y）
   - 应变片到加载点的距离（x）
   - 梁厚度（h）
   - 悬臂梁长度（l）
   - 零应变电阻（R₀）及单位选择
   - 当前电阻（R₁）及单位选择

4. 点击“开始计算”查看结果

## 项目结构
```
foil-strain-gauge-calculation-toolkit/
├── code/
│   └── basic_calculation.py   # 核心计算逻辑
└── web/
    └── basic_calculation/
        ├── app.py             # Web服务器（Flask应用）
        └── templates/
            └── index.html     # Web界面模板
```

## 许可证
[MIT](LICENSE)