# This is an example script for the final.
# Example 2

#Imports
import numpy as np
import mpmath as mp
import math
import pandas as pd
import string
import matplotlib.pyplot as plt
import scipy
from mpl_toolkits.mplot3d import Axes3D
from sympy import Symbol, poly, factor, expand


def main():

# We use x = 24, x = 56, x = 83
    
# Our data set:
# -----------------------------------------------------------------------
    list_x = [22,42,52,82,100]
    list_fx = [4181,4179,4186,4199,4217]

    list_x2 = [10,30,50,70,90]
    list_fx2 = [4192, 4178,4182, 4191, 4208]

    x = 25
    fx = 4180

    z = 85
    fz = 4203

# -----------------------------------------------------------------------

# ======================== x = 25 degrees Celcius ========================
    print('\nWe will be using two data sets of temperatures (nodes) and\
          \nSpecific Heats (nodes evaluated at function).\n\n\n')
    print('--------------------------------------------------------------------------')
    print(' X = 25 DEGREES CELCIUS: \n')
    print('For x = 25 degrees Celcius, we have that our actual Specific Heat is 4180.')
    print('Our nodes (water temperatures) are:            [22,42,52,82,100]')
    print('Our Specific heats evaluated at the nodes are: [4181,4179,4186,4199,4217]')
    print('We now approximate f(x) with several interpolation methods:)')
    print('--------------------------------------------------------------------------\n\n\n')
    print('--------------------------------------------------------------------------')
    print('We will now use Cubic Spline Interpolation with our data set:\n')
    splineConstructor(list_x2, list_fx2, factor_it = 'yes')
    print('We evaluate the necessary spline function to find approximation.\n')
    def c1(x):
        return -9.30357*(0.1*x - 1.0) + 0.000576*(x - 10)**3 + 4192
    
    spline_approx = c1(25)
    print('FINAL APPROXIMATION:', spline_approx)
    print('\nWe find the relative error:\n')
    s1_error = relative_error(4180, spline_approx)
    print('Relative error for Spline: ', s1_error)
    print('--------------------------------------------------------------------------\n\n\n')
# -----------------------------------------------------------------------
    print('--------------------------------------------------------------------------')
    print('We will now use Lagrange Interoplation with our data set:\n')
    abc = lagrange_polynomial(list_x2, list_fx2)
    print(abc)
    print('We evaluate the highest degree Lagrange to find approximation.\n')
    def g1(x):
        return 131*(x - 90)*(x - 70)*(x - 50)*(x - 30)/120000 - 2089*(x - 90)*(x - 70)*(x - 50)\
            *(x - 10)/480000 + 2091*(x - 90)*(x - 70)*(x - 30)*(x - 10)/320000 - \
                1397*(x - 90)*(x - 50)*(x - 30)*(x - 10)/320000 + 263*(x - 70)*(x - 50)*\
                    (x - 30)*(x - 10)/240000
    lag_approx = g1(25)
    print('FINAL APPROXIMATION:', lag_approx)
    print('\nWe find the relative error:\n')
    l1_error = relative_error(4181, lag_approx)
    print('Relative error for Lagrange: ', l1_error)
    print('--------------------------------------------------------------------------\n\n\n')
    print('--------------------------------------------------------------------------')
    
    
# -----------------------------------------------------------------------
    print('We will now use Nevilles method with our data set:')
    nev_approx,n_table = nevillesMethod(x, list_x2, list_fx2, Q_table = None\
                   , individual = 'yes',notable = 'no')
    print(n_table)
    print('\n\n FINAL APPROXIMATION: ', nev_approx)
    print('We consider the Q_4,4 th table entry - The highest degree approximation.\n') 
    print('\nWe find the relative error:\n')
    n1_error = relative_error(4180, nev_approx)
    print('Relative error for Neville: ', n1_error)
    print('--------------------------------------------------------------------------\n\n\n')
# =========================================================================

# ======================== x = 85 degrees Celcius ========================
    print('--------------------------------------------------------------------------')
    print(' X = 85 DEGREES CELCIUS: ')
    print('\nFor x = 85 degrees Celcius, we have that our actual Specific Heat is 4203.')
    print('Our nodes (water temperatures) are:            [10,30,50,70,90]')
    print('Our Specific heats evaluated at the nodes are: [4192,4178,4182,4191,4208]')
    print('We now approximate f(x) with several interpolation methods: ')
    print('--------------------------------------------------------------------------\n\n\n')
    print('--------------------------------------------------------------------------')
    print('\nWe will use now Cubic Spline Interoplation with our data set:\n')
    splineConstructor(list_x2, list_fx2, factor_it='yes')
    print('We evaluate the necessary spline function to find approximation.\n')

    def c(x):
        return 44.75002*(0.0142857142857143*x - 1.0) -\
             0.000263*(x - 70)**3 + 0.015804*(x - 70)**2 + 4191

    spline_approx = c(85)
    print('FINAL APPROXIMATION:', spline_approx)
    print('\nWe find the relative error:\n')
    s1_error = relative_error(4203, spline_approx)
    print('Relative error for Spline: ', s1_error)
    print('--------------------------------------------------------------------------\n\n\n')
    print('--------------------------------------------------------------------------')

# -----------------------------------------------------------------------
    print('We will use now Lagrange Interoplation with our data set:\n')
    abc = lagrange_polynomial(list_x2, list_fx2)
    print(abc)
    print('We evaluate the highest degree Lagrange to find approximation.\n')

    def g(x):
        return 131*(x - 90)*(x - 70)*(x - 50)*(x - 30)/120000 - 2089*(x - 90)*(x - 70)*(x - 50)\
            * (x - 10)/480000 + 2091*(x - 90)*(x - 70)*(x - 30)*(x - 10)/320000 - \
            1397*(x - 90)*(x - 50)*(x - 30)*(x - 10)/320000 + 263*(x - 70)*(x - 50) *\
            (x - 30)*(x - 10)/240000
    lag_approx = g(85)
    print('FINAL APPROXIMATION:', lag_approx)
    print('\nWe find the relative error:\n')
    l1_error = relative_error(4203, lag_approx)
    print('Relative error for Lagrange: ', l1_error)
    print('--------------------------------------------------------------------------\n\n\n')
    print('--------------------------------------------------------------------------')

# -----------------------------------------------------------------------
    print('We will use now Nevilles method with a data set:')
    nev_approx, n_table = nevillesMethod(
        z, list_x2, list_fx2, Q_table=None, individual='yes', notable='no')
    print(n_table)
    print('\n\n FINAL APPROXIMATION: ', nev_approx)
    print('We consider the Q_4,4 th table entry - The highest degree approximation.\n')
    print('\nWe find the relative error:\n')
    n1_error = relative_error(4203, nev_approx)
    print('Relative error for Neville: ', n1_error)
    print('--------------------------------------------------------------------------')
# -----------------------------------------------------------------------
    print('We will use now Hermite method with a data set:')
    herm_approx, n_table = nevillesMethod(
        z, list_x2, list_fx2, Q_table=None, individual='yes', notable='no')
    print(n_table)
    print('\n\n FINAL APPROXIMATION: ', nev_approx)
    print('We consider the Q_4,4 th table entry - The highest degree approximation.\n')
    print('\nWe find the relative error:\n')
    n1_error = relative_error(4203, nev_approx)
    print('Relative error for Neville: ', n1_error)
    print('--------------------------------------------------------------------------')


# =========================================================================
#  Relative error function

def relative_error(actual, approx):
    rel_error = abs(actual - approx) / abs(actual)
    return rel_error

# Spline Interpolation Method

def vec(m): z = [0]*m ; return(z)
def splineConstructor(list_x, list_fx, factor_it = 'yes'):
    n =  len(list_x)
    h = vec(n-1) ; alpha = vec(n-1) ; l = vec(n+1)
    u = vec(n) ; z = vec(n+1) ; b = vec(n) ; c = vec(n+1); d = vec(n)        
    for i in range(0, n - 1):
        h[i] = list_x[i+1] - list_x[i]  
    for i in range(1, n - 1):
        alpha[i] = (3./h[i])*(list_fx[i+1] - list_fx[i])-(3./h[i - 1])*(list_fx[i] - list_fx[i-1])
        l[0] = 1 ; u[0] = 0 ; z[0] = 0
    for i in range(1, n - 1):
        l[i] = 2*(list_x[i+1] - list_x[i-1]) - h[i - 1]*u[i - 1]
        u[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i - 1]*z[i - 1])/l[i]
        l[len(l)-1] = 1 ; z[len(z)-1] = 0 ; c[len(c)-1] = 0
    for j in reversed(range(n - 1)):      
        c[j] = z[j] - u[j]*c[j+1]
        b[j] = (list_fx[j + 1] - list_fx[j])/h[j]- h[j]*(c[j + 1] + 2*c[j])/3.
        d[j] = (c[j + 1] - c[j])/(3*h[j])   
    x = Symbol('x')
    for j in range(0,  n - 1):
        if factor_it == 'no':
            s_jx = round(list_fx[j],6) +  (round(b[j],6)*(x - list_x[j]))             + round(c[j],6)*(x - list_x[j])**2 + round(d[j],6)*(x - list_x[j])**3
            print('S _',j,'(x) =', s_jx, ' for ['                  , list_x[j],',', list_x[j+1],']')
        if factor_it == 'yes':
            s_jx = round(list_fx[j],6) +  factor((round(b[j],6)*(x - list_x[j])))             + round(c[j],6)*(x - list_x[j])**2 + round(d[j],6)*(x - list_x[j])**3
            print('S _',j,'(x) =', s_jx, ' for ['                  , list_x[j],',', list_x[j+1],']')
    return

# Neville's Method
def nevillesMethod(x, list_x, list_fx, Q_table = None, individual = 'no',notable = 'no'):
    n = np.size(list_x) - 1; 
    if (Q_table == None):
        Q_table = np.zeros((n + 1, n + 1));
        
    for i in range(0,n + 1):
        Q_table[i][0] = list_fx[i];
   
    for i in range(1, n + 1):
        for j in np.arange(1, i + 1):
            Q_table[i][j] = 0.0
            Q_table[i][j] += (((x - list_x[i - j])*Q_table[i][j - 1]- (x - list_x[i])*(Q_table[i - 1][j - 1]))/(list_x[i] - list_x[i - j]))
    if individual == 'yes' and i == j:
        print('Q_(',i,',',j,') =',Q_table[i][j])
                
    if notable == 'yes':
        return
    return Q_table[n][n], Q_table; 


# Lagrange Interpolation Method
def lagrange_polynomial(nodes, function_nodes):
    degree_specification = len(nodes) - 1
    x = Symbol("x")
    whole_polynomial = 0
    nodes = nodes[:degree_specification + 1]
    for coefficients in range(0, len(nodes)):
        current_node = nodes[coefficients]
        rest_of_nodes = nodes[:coefficients] + nodes[coefficients + 1:]
        coeffcient_polynomial_numerator = 1
        coeffcient_polynomial_denominator = 1
        for remaining_nodes in rest_of_nodes:
            coeffcient_polynomial_numerator = coeffcient_polynomial_numerator \
                                              * (x - remaining_nodes)
        for remaining_nodes2 in rest_of_nodes:
            coeffcient_polynomial_denominator = coeffcient_polynomial_denominator \
                                                * (current_node - remaining_nodes2)
        coeffient_polynomial = function_nodes[coefficients] \
                               * (coeffcient_polynomial_numerator \
                                  / coeffcient_polynomial_denominator)
        whole_polynomial += coeffient_polynomial
    return whole_polynomial

# Hermite Interpolation Method
def hermite_interpolation_polynomial(x_i, f_xi, f_prime_xi):
    n = np.size(x_i) - 1
    z_array = np.zeros(2 * n + 2)
    q_matrix = np.zeros((2 * n + 2, 2 * n + 2))
    for i in range(0, n + 1):
        z_array[2 * i] = x_i[i]
        z_array[(2 * i) + 1] = x_i[i]
        q_matrix[2 * i][0] = f_xi[i]
        q_matrix[(2 * i) + 1][0] = f_xi[i]
        q_matrix[(2 * i) + 1][1] = f_prime_xi[i]
        if i != 0:
            q_matrix[(2 * i)][1] = (q_matrix[(2 * i)][0] - q_matrix[(2 * i) - 1]
                                    [0]) / (z_array[2 * i] - z_array[(2 * i) - 1])
    for i in range(2, (2 * n) + 2):
        for j in range(2, i + 1):
            q_matrix[i][j] = (q_matrix[i][j - 1] - q_matrix[i - 1]
                              [j - 1]) / (z_array[i] - z_array[i - j])
    print("Approximating polynomial using Hermite Interpolation is {} + {} * (x - {}) + {} * (x - {})^2 + {} * (x - {})^2 * (x - {}) + {} * (x - {})^2 * (x - {})^2".format(
    q_matrix_1c[0][0], q_matrix_1c[1][1], x_i_1c[0], q_matrix_1c[2][2], x_i_1c[0], q_matrix_1c[3][3], x_i_1c[0], x_i_1c[1], q_matrix_1c[4][4], x_i_1c[0], x_i_1c[1]))
    return
# Call the main function.
main()
