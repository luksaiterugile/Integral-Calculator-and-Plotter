import math
import scipy.integrate as integrate
import sympy as syp 
import matplotlib.pyplot as plt

a = 0.0
b = 1.0
N = 4

delta_x = (b - a) / N

alpha_arr = []
# Alpha generation
for i in range(101):
  if(i == 0):
    alpha = 0
  else:
    alpha += 0.01
  alpha_arr.append(alpha)

# True integral
true_integral_areas = []
for alpha in alpha_arr:
  intFxab = ((-2) * math.sin(alpha))/math.pi
  true_integral_areas.append(intFxab)

# Trapezoid integration formula
trapezoid_formula_areas = []
for alpha in alpha_arr:
  area_by_alpha = math.cos(math.pi * a + alpha) + math.cos(math.pi * b + alpha)
  for i in range(1, N):
    xi = a + i * delta_x
    area_by_alpha += 2 * (math.cos(math.pi * xi + alpha))
  area_by_alpha *= delta_x / 2
  trapezoid_formula_areas.append(area_by_alpha)
  area_by_alpha = 0

# Simpson's integration formula
simpson_formula_areas = []
for alpha in alpha_arr:
  area_by_alpha = math.cos(math.pi * a + alpha) + math.cos(math.pi * b + alpha)
  for i in range(1, N):
    xi = a + i * delta_x
    if i % 2 == 0:
      area_by_alpha += 2 * (math.cos(math.pi * xi + alpha))
    else:
      area_by_alpha += 4 * (math.cos(math.pi * xi + alpha))
  area_by_alpha *= delta_x / 3 
  simpson_formula_areas.append(area_by_alpha)
  area_by_alpha = 0

# Display of results
plt.plot(alpha_arr, true_integral_areas, label='True integral')
plt.plot(alpha_arr, simpson_formula_areas, label='Integral by Simpson \
 formula')
plt.plot(alpha_arr, trapezoid_formula_areas, label='Integral by trapezoid \
formula')

plt.title("Plot of integral versus parameters")
plt.xlabel("Alpha value")
plt.ylabel("Integral value")
plt.legend()
plt.savefig("integral-plot.png")

print()
print("Areas of a true integral:", true_integral_areas[0:4])
print("Areas of the trapezium formula:", trapezoid_formula_areas[0:4])
print("Simpson's formula areas:", simpson_formula_areas[0:4])