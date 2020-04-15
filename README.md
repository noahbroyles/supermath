# Supermath
This repo consists of one module I have written in python3 to help you cheat on your next math test, called `supermath.py`.  
  
This is a module meant for importing, not running. Don't be disappointed when you run it and nothing happens. It should work wonders for you though when you import it.

```
class Validate():
```
  This class has four methods: `isLinux()`, `isMac()`, `isWindows()` and `hasLenOf(object, length)`  
 `isLinux()` returns True if you are using a Linux PC.  
 `isMac()` returns True if you are using a Mac.  
 `isWindows()` returns True if you are using a Windows PC.  
 `hasLenOf()` has two parameters called obj and length. It compares the length of an object such as a string or list and returns true if the length = the length param.
 
## Mathematical Functions:  

```
average(listOfNums)
```
  returns the average of a list of numbers  \
    \
    \
    \
  
   
   
    
 
```
mean(listOfNums)
```
  same as average, different name  
  
     
       
        
        
 
```
gcd(a, b)
```
  returns the greatest common denominator of numbers `a` and `b`  
     
       
         
          
  
```
lcm(a, b)
```
  returns the lowest common multiple of numbers `a` and `b`  
  
    
       
          
          
 
```
isRealNumber(number)
```
  returns True if number is real  
     
       
         
         

```
squareRoot(number)
```
  returns the square root of number  
     
        
         
  
```
fastExp(num, pow)
```
  returns num to the pow power using a super efficient algorithm  (I hope)
  
     
       
        

```
quadratic(a, b, c)
```
  returns x, y coordinates of a quadratic equation given `a`, `b`, and `c`  
    
      
       
          
  
```
volSphere(r)
```
  returns the volume of a sphere given radius `r` 
    
      
        
          
           

```
permNote(n, r)
```
  returns `nPr`, `P` standing for permutation notation  
    
     
       
         
          
  
```
combNote(n, r)
```
  returns `nCr`, `C` standing for combination notation  
    
      
        
         
  
```
divideRemain(dividend, divisor)
```
  returns `dividend / divisor` with a remainder instead of a decimal  
    
      
         
           
             
  
```
sin(x), cos(x), tan(x), csc(x), sec(x) cot(x)
```
  all return the corresponding trigonmetric function of number `x` in DEGREES  
    
      
        
          

```
parabolaEquation(xv, yv, xf, yf)
```
  this method returns the equation of a parabola given the x, y coordinates of the vertex and focus.  
  `xv`, `yv` are the x, y coordinates of the vertex  
  `xf`, `yf` are the x, y coordinates of the focus  
    
      
        
         
 
```
areaOfPolygonInCircle(sides, radius)
```
  returns the area of a polygon inscribed in a cricle given the number of sides in the polygon and the radius of the circle  
    
      
        
          
            

```
cramersRule(q, w, e, r, t, y)
```
  returns x, y answers for an algebraic equation, such as: `4x - 5y = 3 and 3x + 2y = -10`. The `q`, `w`, `e`, `r`, `t`, `y` values would be `4, -5, 3, 3, 2, -10` and the method would return `(-1.9130434782608696, -2.130434782608696)`, which is the correct x, y, solution for this equation.  
    
      
        
          
          
```
stats(list)
```
  returns the mean, median, mode, range, standard deviation, and variance of a list of number values  
  
