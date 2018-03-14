from math import acos, pi

def add_vect(v, w):
    '''Adds the values in two lists as vector addition, to 3 decimal places.

    Args:
        two lists of any of (float) or (int), of equal length.
    Returns:
        list.
    '''
    # Create a list of combined elements
    add = list(zip(v, w))
    # Add the elements together to create vector
    add = [round(element[0] + element[1], 3) for element in add]
    return add

def subt_vect(v, w):
    '''Subtracts the values of w from v as vector subtraction, to 3 decimal places.

    Args:
        two lists of any of (float) or (int), of equal length.
    Returns:
        list.
    '''
    # Create a list of combined elements
    subt = list(zip(v, w))
    # Comput v - w for each element
    subt = [round(element[0] - element[1], 3) for element in subt]
    return subt

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

def dot_prod(v, w):
    '''Returns the inner product of two vectors, to 5 decimal places.

    Args:
        two lists of any of (float) or (int), of equal length.
    Returns:
        (float).
    '''
    # Create list of combined elements
    prod = list(zip(v, w))
    # Multiply each set of elements together and return their sum
    prod = round(sum([element[0] * element[1] for element in prod]), 5)
    return prod

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

def para_test(v,w):
    '''Checks the parallelism of two vectors.

    Args:
        two lists of any of (float) or (int), of equal length.
    Returns:
        (bool).
    '''
    # Test for zero vector
    if mag_vect(v) == 0 or mag_vect(w) == 0:
        return True
    elif ang_vect(v, w) == 0 or ang_vect(v,w) == round(pi, 5):
        return True
    return False

def orth_test(v,w):
    '''Checks the orthogonality of two vectors.

    Args:
        two lists of any of (float) or (int), of equal length.
    Returns:
        (bool).
    '''
    if dot_prod(v, w) == 0:
        return True
    return False

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
    para_v = [round(element, 3) for element in para_v]
    return para_v


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


def triangle_area(v, w):
    '''Finds the area of the triangle made by vectors v and w.

    Args:
        two lists of ln() = 3 containing any of (float) or (int).
    Returns:
        float.
    '''
    return parallel_area(v, w)*0.5

if __name__ == "__main__":

    v_1 = [8.218, -9.341]
    v_2 = [-1.129, 2.111]
    v_3 = [7.119, 8.215]
    v_4 = [-8.223, 0.878]
    v_5 = [1.671, -1.012, -0.318]
    v_6 = [-0.221, 7.437]
    v_7 = [8.813, -1.331, -6.247]
    v_8 = [5.581, -2.136]
    v_9 = [1.996, 3.108, -4.554]
    v_10 = [7.887, 4.138]
    v_11 = [-8.802, 6.776]
    v_12 = [-5.955, -4.904, -1.874]
    v_13 = [-4.496, -8.755, 7.103]
    v_14 = [3.183, -7.627]
    v_15 = [-2.668, 5.319]
    v_16 = [7.35, 0.221, 5.188]
    v_17 = [2.751, 8.259, 3.985]
    v_18 = [-7.579, -7.88]
    v_19 = [22.737, 23.64]
    v_20 = [-2.029, 9.97, 4.172]
    v_21 = [-9.231, -6.639, -7.245]
    v_22 = [-2.328, -7.284, -1.214]
    v_23 = [-1.821, 1.072, -2.94]
    v_24 = [2.118, 4.827]
    v_25 = [0, 0]
    v_26 = [3.039, 1.879]
    v_27 = [0.825, 2.036]
    v_28 = [-9.88, -3.264, -8.159]
    v_29 = [-2.155, -9.353, -9.473]
    v_30 = [3.009, -6.172, 3.692, -2.51]
    v_31 = [6.404, -9.144, 2.759, 8.718]
    v_32, v_33 = [8.462, 7.893, -8.187], [6.984, -5.975, 4.778]
    v_34, v_35 = [-8.987, -9.838, 5.031], [-4.268, -1.861, -8.866]
    v_36, v_37 = [1.5, 9.547, 3.691], [-6.007, 0.124, 5.772]

    print("Add vectors:", add_vect(v_1, v_2))
    print("Minus vectors:", subt_vect(v_3, v_4))
    print("Scalar multiplication:", scal_mult(v_5, 7.41))
    print("Vector magnitude:", mag_vect(v_6))
    print("Vector magnitude:", mag_vect(v_7))
    print("Normalization of vector:", norm_vect(v_8))
    print("Normalization of vector:", norm_vect(v_9))
    print("Dot product of two vectors:", dot_prod(v_10, v_11))
    print("Dot product of two vectors:", dot_prod(v_12, v_13))
    print("Angle between two vectors:", ang_vect(v_14, v_15))
    print("Angle between two vectors:", ang_vect(v_16, v_17, False))
    print("Testing para and orth of two vectors:", para_test(v_18, v_19), orth_test(v_18, v_19))
    print("Testing para and orth of two vectors:", para_test(v_20, v_21), orth_test(v_20, v_21))
    print("Testing para and orth of two vectors:", para_test(v_22, v_23), orth_test(v_22, v_23))
    print("Testing para and orth of two vectors:", para_test(v_24, v_25), orth_test(v_24, v_25))
    print("Parallel of v on b:", para_vect(v_26, v_27))
    print("Perpend of v on b:", perp_vect(v_28, v_29))
    print("Parallel & perpend of v on b:", para_vect(v_30, v_31), perp_vect(v_30, v_31))
    print("Cross prod of two vectors:", cross_prod(v_32, v_33))
    print("Area of parallelogram:", parallel_area(v_34, v_35))
    print("Area of triangle:", triangle_area(v_36, v_37))
