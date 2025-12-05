"""
基础值说明
y: 下压距离
x: 应变中心到载荷实施点的距离
h: 载体厚度
l: 悬梁长度
delta_R: 电阻改变值
R_0: 零应变电阻

测试值说明
epsilon: 应变系数 - 无量纲
μ_epsilon: 微应变 - 无量纲
GF: 灵敏度
"""

# 获取变量
y = float(input('输入下压距离y(mm)：'))
x = float(input('输入应变中心到载荷实施点距离x(mm)：'))
h = float(input('输入载体厚度h(mm)：'))
l = float(input('输入悬梁长度l(mm)：'))
R_0 = float(input('输入零应变电阻R_0(Ω)：'))
R_1 = float(input('输入变化后电阻R_1(Ω)：'))
delta_R = R_1 - R_0

# epsilon 应变系数计算函数
def epsilon_calculate():
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    miu_epsilon = epsilon * 1000000
    print(f"epsilon: {epsilon} (Dimensionless)\n μ_epsilon: {miu_epsilon} (Dimensionless)")

# sensitivity 灵敏度计算函数
def gf_sensitivity_calculate():
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    gf = delta_R / (R_0 / epsilon)
    print(f"GF: {gf} (Dimensionless)")

if __name__ == '__main__':
    epsilon_calculate()
    gf_sensitivity_calculate()