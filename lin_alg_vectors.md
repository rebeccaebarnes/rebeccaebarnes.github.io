
### Linear Algebra Refresher: Vectors

More efforts for MDS eligibility - review of linear algebra with Udacity's [Linear Algebra Refresher](https://www.udacity.com/course/linear-algebra-refresher-course--ud953) course. I knew that I had done all of this in high school but didn't have a way to easily show it and knew I needed to brush up anyway. 

**Addition, Subtraction, Scalar Multiplication**

I originally tried to import `Vector` from `vectors` and had such a terrible time getting it to run (installed it, couldn't get it to run, then got it to run, then couldn't get it to run again...) that I just went with using lists as an equivalent for vectors and tuples as an equivalent for points. I might have to do something different when I get to matrices, but for now, this works; I can code it, and it functions in essentially the same way. 

Addition formula:


```python
def add_vect(v, w):
    '''Adds the values in two lists as vector addition, to 3 decimal places.

    Args:
        two lists.
    Returns:
        list.
    '''
    # Create a list of combined elements
    add = list(zip(v, w))
    # Add the elements together to create vector
    add = [round(element[0] + element[1], 3) for element in add]
    return add
```

Subtraction formula:


```python
def subt_vect(v, w):
    '''Subtracts the values of w from v as vector subtraction, 
       to 3 decimal places.

    Args:
        two lists of format [(float), (float)].
    Returns:
        list.
    '''
    # Create a list of combined elements
    subt = list(zip(v, w))
    # Compute v - w for each element
    subt = [round(element[0] - element[1], 3) for element in subt]
    return subt
```

I initially had both of these in a format of:
```
a, b = v[0], v[1]
c, d = w[0], w[1]
add = [a + c, b + d]
```
But realized from zipping in a later formula that this was also possible here (which then caters to vectors of all sizes, which I obviously previously couldn't) and the list comprehension allows for a much more formula for the creation of the final vector. 

Scalar multiplication formula:


```python
def scal_mult(v, x):
    '''Multiplies the values in a list as scalar multiplication,
       to 5 decimal places.

    Args:
        list, (float).
    Return:
        list.
    '''
    # Mutliply each element in the list by x
    v = [round(element * x, 5) for element in v]
    return v
```

And then to test them, answering the course questions:


```python
v_1 = [8.218, -9.341]
v_2 = [-1.129, 2.111]
v_3 = [7.119, 8.215]
v_4 = [-8.223, 0.878]
v_5 = [1.671, -1.012, -0.318]

print(add_vect(v_1, v_2))
print(subt_vect(v_3, v_4))
print(scal_mult(v_5, 7.41))
```

    [7.089, -7.23]
    [15.342, 7.337]
    [12.38211, -7.49892, -2.35638]
    

**Magnitude and Direction**

I've come across this a couple of times now, but what's fascinating to me is to realize that while there are plenty of parts of the math associated with data analysis that seem very familiar, what I have completely forgotten is the notation...

So, to practice my use of LaTex as well, the notation for magnitude of a vector is: $\mid \mid \vec{v} \mid \mid$


Vector magnitude formula:


```python
def mag_vect(v):
    '''Finds the magnitude of a list as a vector, to 5 decimal places.

    Args:
        list.
    Returns:
        (float).
    '''
    # Find the sum of the squares of all elements and the square root of the sum
    mag = round(sum([element ** 2 for element in v]) ** 0.5, 5)
    return mag
```

What's interesting to me is that then, direction is simply referenced by the unit vector, as opposed to the actual angle, while, of course, it's easy to then compute the angle, with arc cos, that is not immediately intuitive to me.

Direction or normalization formula:


```python
def norm_vect(v):
    '''Normalizes the values in a list as a vector, to 5 decimal places.
       Returns an exception if trying to normalize the zero vector.

    Args:
        list.
    Returns:
        list.
    '''
    try:
        # Find the magnitude of v
        n = mag_vect(v)
    except ZeroDivisionError:
        print('You cannot normalize the zero vector.')
    # Normalize v by using scalar multiplication
    v = scal_mult(v, 1/n)
    # Convert back to float
    v = [round(element, 5) for element in v]
    return v
```

(I had originally used an 'if' statement to manage the zero vector ( $\vec{0}$ ), but exception management seemed more elegant, and something to practice)

And to test the formula:


```python
v_6 = [-0.221, 7.437]
v_7 = [8.813, -1.331, -6.247]
v_8 = [5.581, -2.136]
v_9 = [1.996, 3.108, -4.554]

print(mag_vect(v_6))
print(mag_vect(v_7))
print(norm_vect(v_8))
print(norm_vect(v_9))
```

    7.44
    10.884
    [0.934, -0.357]
    [0.34, 0.53, -0.777]
    

**Inner Products**

Now this seems somewhat familiar; more than anything what I remember about linear algebra is learning how to do matrix multiplication, because it was unlike anything I had done before, and obviously calculating the inner product, or dot product, is the first step towards matrix multiplication. 

Dot product formua:


```python
def dot_prod(v, w):
    '''Returns the inner product of two vectors, to 5 decimal places.

    Args:
        two lists of (float) or (int), of equal length.
    Returns:
        (float).
    '''
    # Create list of combined elements
    prod = list(zip(v, w))
    # Multiply each set of elements together and return their sum
    prod = round(sum([element[0] * element[1] for element in prod]), 5)
    return prod
```

Angle between two vectors formula:


```python
from math import acos, pi

def ang_vect(v, w, in_radians=True):
    '''Finds the angle between two vectors in either radians (default) or degrees,
       to 5 decimal places.
       Returns an exception if trying to compare to the zero vector.

    Args:
        v, w: two lists of (float) or (int), of equal length.
        in_radians:
            True: return result in radians (default).
            False: return result in degrees.
    Returns:
        (float).
    '''
    # Test for division by zero
    try:
        norm_v = norm_vect(v)
        norm_w = norm_vect(w)
    except ZeroDivisionError:
        print('You cannot use this formula to compare to the zero vector.')
    # Find the angle of dot product of the normalized vectors
    angle = round(acos(round(dot_prod(norm_v, norm_w), 3)), 5)
    if in_radians is False:
        angle = round(angle*180/pi, 5)
    return angle
```

And again to test the formula:


```python
v_10 = [7.887, 4.138]
v_11 = [-8.802, 6.776]
v_12 = [-5.955, -4.904, -1.874]
v_13 = [-4.496, -8.755, 7.103]
v_14 = [3.183, -7.627]
v_15 = [-2.668, 5.319]
v_16 = [7.35, 0.221, 5.188]
v_17 = [2.751, 8.259, 3.985]

print(dot_prod(v_10, v_11))
print(dot_prod(v_12, v_13))
print(ang_vect(v_14, v_15))
print(ang_vect(v_16, v_17, False))
```

    -41.38229
    56.39718
    3.07201
    60.27631
    

When comparing this to the actual answers in the course, I was getting correct answers for the first two, and not for the second two (I was getting 3.07 and 60.275). After reviewing the answer, I discovered that in the course, the formulae had been adjusted to accommodate the use of actual decimals (due to how floats are otherwise handled by the program). So, I went back and adjusted all of my formula to include this. 


```python
from decimal import Decimal
```

When I ran the updated formulae with Decimal, it didn't improve the results, in fact, the first result for ang_vect was further from the actual (became 3.078) and the second remained unchanged. I wanted to see if this was due to rounding errors (originally everything was rounded to three decimals because this is what was required for our answers), or whether it was due to imprecision due to lack of use of the Decimal (without which, apparently can cause an error for finding the acos of some normalized dot products).

So I ran some tests:


```python
print(dot_prod(norm_vect([1, 1, 1]), norm_vect([5, 5, 5])))
print(dot_prod(norm_vect([-1, -1, -1]), norm_vect([-5, -5, -5])))
```

    0.999
    0.999
    

This is definitely a problem, because obviously the product of these should be 1 and not 0.999. So, back to testing.


```python
print(norm_vect([1, 1, 1]), norm_vect([5, 5, 5]))
print(norm_vect([-1, -1, -1]), norm_vect([-5, -5, -5]))
```

    [Decimal('0.577'), Decimal('0.577'), Decimal('0.577')] [Decimal('0.577'), Decimal('0.577'), Decimal('0.577')]
    [Decimal('-0.577'), Decimal('-0.577'), Decimal('-0.577')] [Decimal('-0.577'), Decimal('-0.577'), Decimal('-0.577')]
    

So, `0.577 * 0.577` gives `0.332929` on my calculator, and multiplied by 3, gives `0.998787`. When this is rounded to three decimal places, it gives `0.999`, which was the answer above. So it would seem that the error is a rounding error that is affecting normalizing (reminding me why my Grade 10 math teacher would always encourage us to round to more significant values when computing for the final answer). 

Because of this, I adjusted the rounding to 5. I also noted that the results of norm_vect are Decimal types, so I converted them back to floats just for ease of presentation.

After doing all of this, I reran everything and got the answers I was looking for! I realized that due to the rounding, I probably caused most of my errors (and wasn't certain about the impact of the Decimal), but, it works - I double checked against the previous test results for the dot products:


```python
print(dot_prod(norm_vect([1, 1, 1]), norm_vect([5, 5, 5])))
print(dot_prod(norm_vect([-1, -1, -1]), norm_vect([-5, -5, -5])))
```

    1.00000
    1.00000
    

I realize that if I were to use these formulae for applications that required more precision, they likely wouldn't be appropriate, but I believe for my current purposes they are functional. I expect that in the future, if I am using linear algebra I will use the Vector module (or I believe there are options in numpy), but for now, I think that this suffices. 

**Parallelism & Orthogonality**

So after this impressive simplifed walkthrough of the proof (from the Udacity course) for why $\vec{0}$ is orthogonal to itself (the only vector for which this is the case):

$$
\begin{align}
if \quad \vec{v}.\vec{v} \, = \, 0\\
\therefore \; \mid \mid \vec{v} \mid \mid ^2 \, = \, 0\\
\therefore \; \mid \mid \vec{v} \mid \mid \; = \, 0\\
\therefore \, \vec{v} \, = \, \vec{0}\\
\end{align}
$$
<p style="text-align: center;">(because $\vec{0}$ is the only vector with 0 magnitude)</p>

It was time to put my formula to the true test!


```python
def para_test(v,w):
    '''Checks the parallelism of two vectors.

    Args:
        two lists of (float) or (int).
    Returns:
        (bool).
    '''
    # Test for zero vector
    if mag_vect(v) == 0 or mag_vect(w) == 0:
        return True
    elif ang_vect(v, w) == 0 or ang_vect(v,w) == round(pi, 5):
        return True
    return False
```


```python
def orth_test(v,w):
    '''Checks the orthogonality of two vectors.

    Args:
        two lists of (float) or (int).
    Returns:
        (bool).
    '''
    if dot_prod(v, w) == 0:
        return True
    return False
```


```python
v_18 = [-7.579, -7.88]
v_19 = [22.737, 23.64]
v_20 = [-2.029, 9.97, 4.172]
v_21 = [-9.231, -6.639, -7.245]
v_22 = [-2.328, -7.284, -1.214]
v_23 = [-1.821, 1.072, -2.94]
v_24 = [2.118, 4.827]
v_25 = [0, 0]

print(para_test(v_18, v_19), orth_test(v_18, v_19))
print(para_test(v_20, v_21), orth_test(v_20, v_21))
print(para_test(v_22, v_23), orth_test(v_22, v_23))
print(para_test(v_24, v_25), orth_test(v_24, v_25))
```

    True False
    False False
    False True
    True True
    

Completing the above took **forever** in part because of my lack of coding experience, and in part, for imperfect conceptualisation of parallelism, and then the imprecision came into play. 

Firstly, I tried to create a function that could manage both tests but kept overwriting the results of one test with the other, especially when the zero vector was involved. I finally worked out that it was easier to test them separately and manage the comparison to th null vector for parallelism. 

Also tried developing all of the code here instead of in my editor which was a bad move, I found it harder to navigate around the code here, so the editor is staying in use after this!

Next, I was trying to compare the magnitudes of the vectors for parallelism, but normalizing and finding the absolute, but it's much easier to just compare the angles (as I found out in the answers), which will either be zero or $\pi$ radians. 

Finally, the rounding issue played again, which allowed me to finally sort out that, yes, the issue had to do with the rounding, but that as long as I appropriately managed the rounding (rounding to longer than I was intending to compare), I could use it, and I didn't need the Decimal at all. Again, of course this won't work in more precise applications, but it is fine for now. So all formulae were converted back (!) to not using Decimal. 

**Projecting Vectors**

Projecting vectors also tweaked the memory files. Calculating the parallel and perpendicular elements of a vector projected onto another reminded me of gravitational forces acting on an inclined plane. (I'm pretty sure in 2D it's the same, but it gets complicated after that) 

One explanation that I like is that parallel component of $\vec{v}$ (if $\vec{v}$ is projected onto $\vec{b}$) is that the parallel component of $\vec{v}$ is like the shadow made by $\vec{v}$ onto $\vec{b}$ if the sun were shining directly on top of $\vec{b}$. 

The notation for $\vec{v}$ being projected onto $\vec{b}$, or, the normalization of $\vec{v}$ onto $\vec{b}$ is:

$$
proj_ \vec{b} ( \, \vec{v} \, ) \, 
\\
$$

$$
or 
\\
$$

$$
\vec{v} \, ^\parallel
$$

That is, "v parallel".

The part of $\vec{v}$ that is not projected onto $\vec{b}$, and is perpendicular - or orthogonal - to $\vec{b}$ is known as $\vec{v} \, ^ \perp$, or, "v perp".

Again, following the nice walk-thru provided in the class for the calculation of the magnitude, or length, of $\vec{v} \, ^\parallel$ (assumption: $\theta \; \leqslant 90^o$):

$$
(1) \quad cos \, \theta \, = \, 
\frac{\| \vec{v} \, ^\parallel \|} 
{\| \vec{v} \|}
\\
and
\\
(2) \quad cos \, \theta \quad = \quad \frac{\vec{v}.\vec{b}}
{\| \vec{v} \| \, \| \vec{b} \|}
\\
$$

$$
rearrange \; (1)
\\
$$

$$
\| \vec{v} \, ^\parallel \| \quad = \quad \| \vec{v} \| \, cos \theta
\\
$$

$$
sub \; (2) \; into \; (1)
\\
\therefore \; \| \vec{v} \, ^\parallel \| \quad = \quad
\| \vec{v} \|
\frac{\vec{v}.\vec{b}}
{\| \vec{v} \| \| \vec{b} \|}
\\
$$

$$
\therefore \; \| \vec{v} \, ^\parallel \| \quad = \quad \vec{v}. \vec{u} \, _\vec{b}
$$

That is, the length of $\vec{v}$ equals the dot product of $\vec{v}$ and $\vec{b}$ normalized (divided by it's magnitude), or, the unit vector.

Because $\vec{v} \, ^\parallel$ points in the same direction as $\vec{u} \, _\vec{b}$, if we scale the unit vector by $\| \vec{v} \|$, we will get $\vec{v} \, ^\parallel$.

That is:

$$
\vec{v} \, ^\parallel \; = \; \| \vec{v} \, ^\parallel \| . \vec{u} \, _\vec{b}
$$

By plugging in the formula (from above) for $\| \vec{v} \, ^\parallel \|$, the resulting formula is:

$$
\vec{v} \, ^\parallel \; = \; (\vec{v}.\vec{u} \, _\vec{b} ). \vec{u} \, _\vec{b}
$$

This will work even if the angle between $\vec{v}$ and $\vec{b}$ is not less than $90^o$.

Phew!! Now to get to the coding for calculating the parallel and orthogonal components of a vector projected onto another:


```python
def para_vect(v, b):
    '''Returns the parallel component of v projected onto b.

    Args:
        two lists of the same length containing any of (float) or (int).
    Returns:
        list.
    '''
    # Find the normalization of b
    try:
        norm_b = norm_vect(b)
    except ZeroDivisionError:
        print('There is no component of a vector that projects onto the zero vector.')
    x = dot_prod(v, norm_b)
    para_v = scal_mult(norm_b, x)
    return para_v
```


```python
def perp_vect(v, b):
    '''Returns the perpendicular component of v projected onto b.

    Args:
        two lists of the same length containing any of (float) or (int).
    Returns:
        list.
    '''
    # Find v parallel
    try:
        para_v = para_vect(v, b)
    except:
        print('There may not be a unique perpendicular component of v.')
    # Subtract para_v from v to find v perp
    return subt_vect(v, para_v)
```


```python
v_26 = [3.039, 1.879]
v_27 = [0.825, 2.036]
v_28 = [-9.88, -3.264, -8.159]
v_29 = [-2.155, -9.353, -9.473]
v_30 = [3.009, -6.172, 3.692, -2.51]
v_31 = [6.404, -9.144, 2.759, 8.718]

print("Parallel of v on b:", para_vect(v_26, v_27))
print("Perpend of v on b:", perp_vect(v_28, v_29))
print("Parallel & perpend of v on b:", para_vect(v_30, v_31), perp_vect(v_30, v_31))
```

    Parallel of v on b: [1.08262, 2.67173]
    Perpend of v on b: [-8.35, 3.376, -1.434]
    Parallel & perpend of v on b: [1.96851, -2.81077, 0.84807, 2.67983] [1.04, -3.361, 2.844, -5.19]
    

I did really well for the code that I defined and it worked properly, I just forgot to add management for attempting to project onto the zero vector for para_vect and for if there was no unique component for $\vec{v} \, ^\perp$. I'm uncertain exactly what error would be thrown (or how to cause it to be thrown), so I broadly covered it with my exception management. 

**Cross Products**

So they walked through the proof/derivation of the formula for this and I could NOT follow it. But, the result of the cross product of two vectors works like this:
$$
if \quad \vec{v} \; = \; \left\lgroup \matrix{x_1\cr y_1\cr z_1} \right\rgroup
\; , \quad \vec{w} \; = \; \left\lgroup \matrix{x_2\cr y_2\cr z_2} \right\rgroup
\; , \quad then \quad \vec{v} \, \times \, \vec{w} \; = \; 
\left\lgroup \matrix{y_1 z_2 \; - \; y_2 z_1\cr -(x_1 z_2 \; - \; x_2 z_1)\cr x_1 y_2 \; - \; x_2 y_1} \right\rgroup
$$

Basically the way this works is you do a bunch of multiply these crosses of this pair, and subtract by the other cross of the pair, for each of the potential paris within the two vectors. 

The area of the parallelogram formed by $\vec{v}$ and $\vec{w}$ is $\|\vec{v} \, \times \, \vec{w} \|$. The area of the triangle within the parallelogram is half of this. 

And back to coding:


```python
def cross_prod(v, w):
    '''Finds the vector that is orthogonal to both v and w, or the cross-product.

    Args:
        two lists of ln() = 3 containing any of (float) or (int).
    Returns:
        list.
    '''
    # Complete the cross product multiplications and subtractions
    try:
        x_line = round(v[1]*w[2] - w[1]*v[2], 5)
        y_line = round(w[0]*v[2] - v[0]*w[2], 5)
        z_line = round(v[0]*w[1] - w[0]*v[1], 5)
    except ValueError as e:
        msg = str(e)
        if msg == 'need more than 2 values to unpack':
            v.append(0)
            w.append(0)
            x_line = round(v[1]*w[2] - w[1]*v[2], 5)
            y_line = round(w[0]*v[2] - v[0]*w[2], 5)
            z_line = round(v[0]*w[1] - w[0]*v[1], 5)
            return [x_line, y_line, z_line]
        elif (msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
            print('This function is only designed to work in two 3D spaces')
        else:
            raise e

    return [x_line, y_line, z_line]
```


```python
def parallel_area(v, w):
    '''Finds the area of the parallelogram made by vectors v and w.

    Args:
        two lists of ln() = 3 containing any of (float) or (int).
    Returns:
        float.
    '''
    # Find the cross product of v and w
    parallel = cross_prod(v, w)
    # Find the area of the parallelogram
    return mag_vect(parallel)
```


```python
def triangle_area(v, w):
    '''Finds the area of the triangle made by vectors v and w.

    Args:
        two lists of ln() = 3 containing any of (float) or (int).
    Returns:
        float.
    '''
    return parallel_area(v, w)*0.5
```


```python
v_32, v_33 = [8.462, 7.893, -8.187], [6.984, -5.975, 4.778]
v_34, v_35 = [-8.987, -9.838, 5.031], [-4.268, -1.861, -8.866]
v_36, v_37 = [1.5, 9.547, 3.691], [-6.007, 0.124, 5.772]

print("Cross prod of two vectors:", cross_prod(v_32, v_33))
print("Area of parallelogram:", parallel_area(v_34, v_35))
print("Area of triangle:", triangle_area(v_36, v_37))
```

    Cross prod of two vectors: [-11.20457, -97.60944, -105.68516]
    Area of parallelogram: 142.12222
    Area of triangle: 42.56494
    

Although the lesson mentioned accommodating for vectors of ln() = 2, I had no idea how to do it, so I followed the exception management provided in the lesson, adapting it to my situation.

**The next section will be on Intersections!**
