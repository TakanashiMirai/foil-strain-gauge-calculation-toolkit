import pandas as pd
import matplotlib.pyplot as plt
import os
import re

def process_resistance(value):
    """处理电阻值，提取数值并转换单位（MΩ、kΩ -> Ω）"""
    # 转换为字符串处理，兼容数字或带单位的情况
    value_str = str(value).strip().lower()  # 转为小写便于统一判断单位（m、k）

    # 提取数值部分（支持正负号、小数点，如"123.45MΩ"提取"123.45"）
    num_match = re.search(r'[-+]?\d+\.?\d*', value_str)
    if not num_match:
        raise ValueError(f"无效的电阻值格式：{value}，无法提取数值")
    num = float(num_match.group())

    # 处理单位：根据单位转换为Ω
    if 'M' in value_str:  # 兆欧（MΩ）转换：1MΩ = 1e6Ω
        num *= 1000000
    elif 'M次'in value_str:
        num *= 1000000
    elif 'k' in value_str:  # 千欧（kΩ）转换：1kΩ = 1e3Ω
        num *= 1000
    elif 'k次' in value_str:
        num *= 1000
    # 若不含单位或含Ω，默认单位为Ω，不做转换

    return num


def plot_resistance_change():
    # 获取零应变电阻R_0（单位：Ω）
    R_0 = float(input('输入零应变电阻 R_0(Ω)：'))

    # 获取CSV文件路径并读取数据
    while True:
        file_path = input('请输入实验数据CSV文件路径：')
        if os.path.exists(file_path):
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
                # 提取第三列数据并处理（转换为数值，统一单位为Ω）
                R_1_raw = df.iloc[:, 2].values  # 原始数据（可能是字符串或混合类型）
                R_1_values = []
                for val in R_1_raw:
                    try:
                        processed = process_resistance(val)
                        R_1_values.append(processed)
                    except ValueError as e:
                        print(f"跳过无效数据：{e}")

                # 最多取120个有效数据点（对应120秒）
                n_points = min(len(R_1_values), 120)
                R_1_values = R_1_values[:n_points]
                if not R_1_values:
                    print("没有有效电阻数据，请检查文件内容")
                    continue
                break
            except Exception as e:
                print(f"读取文件出错：{e}，请重新输入")
        else:
            print("文件不存在，请重新输入")

    # 生成时间数据（0到n-1秒）
    times = range(n_points)

    # 计算ΔR/R₀百分比（ΔR = R₁ - R₀，单位均为Ω，确保计算正确）
    delta_R_over_R0_percent = [((r1 - R_0) / R_0) * 100 for r1 in R_1_values]

    # 创建图表
    plt.figure(figsize=(10, 6))
    plt.plot(times, delta_R_over_R0_percent, linestyle='-', color='b', markersize=4)

    # 设置图表属性
    plt.xlabel('Time (s)')
    plt.ylabel(r'$(\Delta R / R_0)$ (%)')
    plt.title('Curve of resistance change rate over time')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xlim(0, max(times) if times else 0)
    plt.xticks(range(0, max(times) + 1, 10) if times else [0])  # 每10秒一个刻度

    # 显示图表
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_resistance_change()