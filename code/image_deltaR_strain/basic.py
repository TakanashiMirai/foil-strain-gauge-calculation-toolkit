import pandas as pd
import matplotlib.pyplot as plt
import os
import re
import numpy as np
from scipy import stats

def process_resistance(value):
    """处理电阻值，提取数值并转换单位（MΩ、kΩ -> Ω）"""
    value_str = str(value).strip().lower()

    # 提取数值部分
    num_match = re.search(r'[-+]?\d+\.?\d*', value_str)
    if not num_match:
        raise ValueError(f"无效的电阻值格式：{value}，无法提取数值")
    num = float(num_match.group())

    # 处理单位
    if 'M' in value_str:  # 兆欧（MΩ）转换：1MΩ = 1e6Ω
        num *= 1000000
    elif 'M次'in value_str:
        num *= 1000000
    elif 'k' in value_str:  # 千欧（kΩ）转换：1kΩ = 1e3Ω
        num *= 1000
    elif 'k次' in value_str:
        num *= 1000

    return num


def epsilon_calculate(y, x, h, l):
    """计算应变变系数和微应变"""
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    miu_epsilon = epsilon * 1000000  # 微应变
    return epsilon, miu_epsilon


def generate_equally_spaced_ys(start_y, end_y, num_points):
    """生成等值变化的y值"""
    return np.linspace(start_y, end_y, num_points)


def plot_strain_vs_resistance_change():
    # 获取输入参数
    print("请输入以下参数：")
    start_y = float(input('输入起始自由端挠度 y_start(mm)：'))
    end_y = float(input('输入结束自由端挠度 y_end(mm)：'))
    x = float(input('输入应变计中心到载荷点的距离 x(mm)：'))
    h = float(input('输入梁厚度 h(mm)：'))
    l = float(input('输入悬臂梁长度 l(mm)：'))
    R_0 = float(input('输入零应变电阻 R_0(Ω)：'))

    # 获取CSV文件路径并读取数据
    while True:
        file_path = input('请输入实验数据CSV文件路径：')
        if os.path.exists(file_path):
            # 替换原读取文件的try块内容
            try:
                # 尝试常见编码（utf-8、gbk、gb2312）
                encodings = ['utf-8', 'gbk', 'gb2312']
                for encoding in encodings:
                    try:
                        df = pd.read_csv(file_path, encoding=encoding)
                        break
                    except UnicodeDecodeError:
                        continue
                else:
                    # 所有编码都尝试失败
                    raise ValueError("无法识别文件编码，请确认文件格式为CSV且编码正确")

                R_1_raw = df.iloc[:, 2].values  # 第三列是电阻数据
                R_1_values = []
                for val in R_1_raw:
                    try:
                        processed = process_resistance(val)
                        R_1_values.append(processed)
                    except ValueError as e:
                        print(f"跳过无效数据：{e}")

                if not R_1_values:
                    print("没有有效电阻数据，请检查文件内容")
                    continue
                break
            except Exception as e:
                print(f"读取文件出错：{e}，请重新输入")
        else:
            print("文件不存在，请重新输入")

    # 生成等值变化的y值
    num_points = len(R_1_values)
    y_values = generate_equally_spaced_ys(start_y, end_y, num_points)

    # 计算相关参数
    delta_R = [r1 - R_0 for r1 in R_1_values]
    delta_R_over_R0_percent = [(dr / R_0) * 100 for dr in delta_R]
    strains = []
    epsilons = []

    for y in y_values:
        epsilon, miu_epsilon = epsilon_calculate(y, x, h, l)
        strains.append(miu_epsilon)
        epsilons.append(epsilon)

    # 计算GF值（灵敏度）
    valid_indices = [i for i, eps in enumerate(epsilons) if eps != 0]
    if valid_indices:
        avg_gf = np.mean([(delta_R[i] / R_0) / epsilons[i] for i in valid_indices])
    else:
        avg_gf = 0

    # 线性拟合
    slope, intercept, r_value, p_value, std_err = stats.linregress(strains, delta_R_over_R0_percent)
    r_squared = r_value ** 2
    fit_line = [slope * x + intercept for x in strains]

    # 创建图表
    plt.figure(figsize=(10, 6))

    # 绘制数据点
    plt.scatter(strains, delta_R_over_R0_percent, color='blue', label='Data points')

    # 绘制拟合线
    plt.plot(strains, fit_line, 'r--', label=f'Fitting line: y = {slope:.6f}x + {intercept:.6f}')

    # 添加文本标注
    plt.text(0.05, 0.95, f'R² = {r_squared:.6f}', transform=plt.gca().transAxes,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    plt.text(0.05, 0.85, f'GF = {avg_gf:.6f}', transform=plt.gca().transAxes,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 设置图表属性
    plt.xlabel('Microstrain (μɛ)')
    plt.ylabel(r'$(\Delta R / R_0)$ (%)')
    plt.title('Graph of the Relationship Between Microstrain and Resistance Change Rate')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 显示图表
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_strain_vs_resistance_change()