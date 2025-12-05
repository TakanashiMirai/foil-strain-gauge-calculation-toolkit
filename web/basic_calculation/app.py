from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_epsilon(y, x, h, l):
    """计算应变系数及微应变"""
    epsilon = (3 * y * h * x) / (2 * pow(l, 3))
    miu_epsilon = epsilon * 1000000
    return epsilon, miu_epsilon

def calculate_gf(delta_R, R_0, epsilon):
    """计算灵敏度"""
    gf = (delta_R / R_0) / epsilon
    return gf

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # 获取表单数据
            y = float(request.form['y'])
            x = float(request.form['x'])
            h = float(request.form['h'])
            l = float(request.form['l'])
            R0 = float(request.form['R0'])
            R1 = float(request.form['R1'])
            delta_R = R1 - R0

            # 执行计算
            epsilon, miu_epsilon = calculate_epsilon(y, x, h, l)
            gf = calculate_gf(delta_R, R0, epsilon)

            # 整理结果
            result = {
                'epsilon': round(epsilon, 8),
                'miu_epsilon': round(miu_epsilon, 2),
                'gf': round(gf, 4)
            }
        except ValueError:
            result = "输入错误，请确保所有字段都是有效的数字"
        except ZeroDivisionError:
            result = "计算错误，悬梁长度不能为零"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)