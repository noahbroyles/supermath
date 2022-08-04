# Supermath
This repo consists of one module I have written in python3 to help you cheat on your next math test, called `supermath.py`.  
<br>
## Mathematical Functions:  

```
average(listOfNums)
```
  returns the average of a list of numbers  
<br><br>
 
```
mean(listOfNums)
```
  same as average, different name  
<br><br>
    
 
```
gcd(a, b)
```
  returns the greatest common denominator of numbers `a` and `b`
<br><br>
  
```
lcm(a, b)
```
  returns the lowest common multiple of numbers `a` and `b`  
<br><br>    

```
is_real_number(number)
```
  returns True if number is real  
<br><br>  
    
 
```
square_root(number)
```
  returns the square root of number  
    
<br><br>
 
```
fast_exp(num, pow)
```
  returns num to the pow power using a super efficient algorithm  (I hope)  
    
<br><br>
 
```
quadratic(a, b, c)
```
  returns x, y coordinates of a quadratic equation given `a`, `b`, and `c`  
    
<br><br>
 
```
vol_sphere(r)
```
  returns the volume of a sphere given radius `r`  
    
<br><br>

```
permutation_notation(n, r)
```
  returns `nPr`, `P` standing for permutation notation  
       
<br><br>
 
```
combination_notation(n, r)
```
  returns `nCr`, `C` standing for combination notation  
<br><br>
    
 
```
divide_remain(dividend, divisor)
```
  returns `dividend / divisor` with a remainder instead of a decimal  
<br><br>
 
```
sin(x), cos(x), tan(x), csc(x), sec(x) cot(x)
```
  all return the corresponding trigonmetric function of number `x` in DEGREES  
<br><br>
 
```
parabola_equation(xv, yv, xf, yf)
```
  this method returns the equation of a parabola given the x, y coordinates of the vertex and focus.  
  `xv`, `yv` are the x, y coordinates of the vertex  
  `xf`, `yf` are the x, y coordinates of the focus  
     
<br><br>
 
```
area_of_polygon_in_circle(sides, radius)
```
  returns the area of a polygon inscribed in a cricle given the number of sides in the polygon and the radius of the circle  \
     
<br><br>
 
```
cramers_rule(q, w, e, r, t, y)
```
  returns x, y answers for an algebraic equation, such as: `4x - 5y = 3 and 3x + 2y = -10`. The `q`, `w`, `e`, `r`, `t`, `y` values would be `4, -5, 3, 3, 2, -10` and the method would return `(-1.9130434782608696, -2.130434782608696)`, which is the correct x, y, solution for this equation.  
     
<br><br>

```
stats(list)
```
  returns the mean, median, mode, range, standard deviation, and variance of a list of number values  
  
