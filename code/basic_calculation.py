"""
基础值说明
y: 自由端挠度
x: 应变计中心到载荷点的距离
h: 梁厚度
l: 悬臂梁长度
R_0: 零应变电阻
R_1: 当前电阻

测试值说明
delta_R: 电阻改变值
epsilon: 应变系数 - 无量纲
μ_epsilon: 微应变 - 无量纲
GF: 灵敏度
"""

# 获取变量
y = float(input('输入自由端挠度 y(mm)：'))
x = float(input('输入应变计中心到载荷点的距离 x(mm)：'))
h = float(input('输入梁厚度 h(mm)：'))
l = float(input('输入悬臂梁长度 l(mm)：'))
R_0 = float(input('输入零应变电阻 R_0(Ω)：'))
R_1 = float(input('输入当前电阻 R_1(Ω)：'))
delta_R = R_1 - R_0

# epsilon 应变系数计算函数
def epsilon_calculate():
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    miu_epsilon = epsilon * 1000000
    print(f"epsilon: {epsilon} (Dimensionless)\n μ_epsilon: {miu_epsilon} (Dimensionless)")

    return epsilon, miu_epsilon

# sensitivity 灵敏度计算函数
def gf_sensitivity_calculate():
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    gf = (delta_R / R_0) / epsilon
    print(f"GF: {gf} (Dimensionless)")

    return gf

if __name__ == '__main__':
    epsilon_calculate()
    gf_sensitivity_calculate()