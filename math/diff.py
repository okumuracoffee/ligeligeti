# 一階微分方程式
import sympy
from sympy.plotting import plot
sympy.init_printing(use_unicode=True)
#%matplotlib inline
x = sympy.Symbol('x')   # 変数を定義
expr = 2 * x ** 2 + 5 * x - 3
plot(expr, (x, -20, 20)) # グラフを描画
print (sympy.diff(expr))

plot(sympy.diff(expr), (x, -20, 20)) # グラフを描画