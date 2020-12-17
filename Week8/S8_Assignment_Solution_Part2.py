# write a python program to multiply three numbers
num1 = 1.5
num2 = 6.3
num3 = -2.3
product = num1 * num2 * num3
print(f'Product: {product}')


# write a python function that when given two numbers, would divide the first number by second number and return the quotient and remainder
def divide_first_number_by_second(num1, num2):
    return (num1 // num2), (num1 % num2)


# write a python function to return the largest and smallest numbers in the given list and return None if the list is empty
def largest_and_smallest(list_of_nums):
    if list_of_nums:
        return max(list_of_nums), min(list_of_nums)
    else:
        return

# write a python function that would read the given input file path and print its contents
def read_and_print_file(filepath):
    with open(filepath, "r") as infile:
        print( infile.read() )


# write a python program that would print the first n positive integers using a for loop
n = 62
for num in range(n):
    print(num)


# write a python function that returns the input list sorted in ascending order
def sort_ascending(list_to_be_sorted):
    return sorted(list_to_be_sorted)


# write a python function that returns the input list sorted in descending order
def sort_descending(list_to_be_sorted):
    return sorted(list_to_be_sorted, reverse=True)


# write a python function that would return the sum of first n natural numbers, where n is the input
def sum_first_n(n):
    return ( n * (n+1) ) // 2


# write a recursive python function that would return the sum of first n natural numbers, where n is the input
def sum_first_n_recursive(n):
    if n == 0:
        return 0
    return sum_first_n_recursive(n-1) + n


# write a python function that would filter a list of dictionaries where a specified key equals given value, list_of_dictionaries, key and value are inputs to this function.
def filter_with_key_value(list_of_dicts, key, value):
    return list( filter( lambda x: x.get(key) == value, list_of_dicts ) )


# write a recursive python function that takes either a list or tuple as input and reverses the order of its elements
def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()
    if seq == emptySeq:
        return emptySeq
    restrev = reverse(seq[1:])
    first = seq[0:1]
    result = restrev + first
    return result


# write a python function that returns the square of a given input number
def square(x):
    return x**2


# write a python function that performs selection sort on the given list or tuple or string and returns the new sorted sequence
def selection_sort(list_to_be_sorted):
    sorted_list = list_to_be_sorted[:]
    for i in range(len(sorted_list)):
        new_min = sorted_list[i]
        new_min_old_place = i
        for j in range(i+1, len(sorted_list)):
            if new_min > sorted_list[j]:
                new_min = sorted_list[j]
                new_min_old_place = j
        old_val = sorted_list[i]
        sorted_list[i] = new_min
        sorted_list[new_min_old_place] = old_val
    return sorted_list


# write a python program that asks for user input and prints the given input
a = input("User Input")
print(a)


# write a python function shifts and scales all numbers in the given list by the given mean and standard deviation
def shift_and_scale(list_of_nums, mean, std):
    return [ (x-mean) / std for x in list_of_nums ]


# write a python function that takes in a list of sequences and zips each corresponding element from the list into a tuple and returns the list of such tuples
def zip_(list_of_seq):
    return list(zip(*list_of_seq))


# write a python program that asks user to guess a number between 1 and 5 and guess it within 3 guesses
print("Please guess a number between 1 and 5 and I will guess within 3 chances!")
guess1 = input("Is it <= 3? enter y/n \n")
if guess1 == "y":
    guess2 = input("Is it <= 2? enter y/n \n")
    if guess2 == "y":
        guess3 = input("Is it 1? enter y/n \n")
        if guess3 == "y":
            print("Yay! found the number, its 1")
        else:
            print("Yay! found the number, its 2")
    else:
        print("Yay! found the number, its 3")
else:
    guess2 = input("Is it 4? enter y/n \n")
    if guess2 == "y":
        print("Yay! found the number, its 4")
    else:
        print("Yay! found the number, its 5")


# write python program that would merge two dictionaries by adding the second one into the first
a = {"a": 1, "b": 3}
b = {"c": 1, "d": 3}
a.update(b)


# write a python function that would reverse the given string
def reverse_string(str_to_be_reversed):
    return str_to_be_reversed[::-1]


# write a python program that would print "Hello World"
print("Hello World")


# write a python program that would swap variable values
a = 10
b = 15
a, b = b, a


# write a python program that iterates over a dictionary and prints its keys and values
a = {"a":1, "b":2, "c":3, "d":4}
for k, v in a.items():
    print(k, v)


# write a python function that would print the ASCII value of a given character
def print_ascii(char):
    print(ord(char))


# write a python function that takes in two numbers and returns their HCF
def hcf(num1, num2):
    smaller = num1 if num1 < num2 else num2
    for i in range(1, smaller+1):
        if (num1 % i == 0) and (num2 % i == 0):
            hcf = i
    return hcf


# write a python function that takes in two numbers and returns their LCM
def lcm(num1, num2):
    bigger = num1 if num1 > num2 else num2
    while True:
        if (bigger % num1 == 0) and (bigger % num2 == 0):
            break
        bigger += 1
    return bigger


# write a recursive python function to calculate sum of natural numbers upto n, where n is an argument
def recursive_sum(n):
    if n <= 1:
        return n
    else:
        return n + recursive_sum(n-1)


# write a python function that deletes the last element of a list and returns the list and the deleted element
def delete_last_element(list_to_be_processed):
    deleted_element = list_to_be_processed.pop()
    return list_to_be_processed, deleted_element


# write a python function that takes in a list and returns a list containing the squares of the elements of the input list
def square_list_elements(list_to_be_squared):
    return list( map(lambda x: x**2, list_to_be_squared) )


# write a python function that finds square roots of a given number, if the square root is an integer, else returns the message "Error - the square root is not an integer"
def find_integer_square_roots(num):
    found = False
    for k in range(1, (num//2)+1):
        if ((k**2)==num):
            found = True
            break
    if not found:
        return "Error - the square root is not an integer"
    return -k, k


# write a python program that prints out natural numbers less than or equal to the given number using a while loop
input_num = 27
while input_num:
    print(input_num)
    input_num -= 1


# write a python function that takes two numbers. The function divides the first number by the second and returns the answer. The function returns None, if the second number is 0
def divide(num1, num2):
    if num2 == 0:
        return
    else:
        return num1 / num2


# write a python program uses else with for loop
seq = "abcde"
for k in seq:
    if k == "f":
        break
else:
    print("f Not Found!")


# write a recursive python function that performs merge sort on the given list or tuple or string and returns the new sorted sequence
def sort_and_merge(l1, l2):
    new_list = []
    i = 0
    j = 0
    l1_len = len(l1)
    l2_len = len(l2)
    while (i <= l1_len-1) and (j <= l2_len-1):
        if l1[i] < l2[j]:
            new_list.append(l1[i])
            i +=1
        else:
            new_list.append(l2[j])
            j +=1
    if i <= (l1_len-1):
        new_list += l1[i:]
    if j <= (l2_len-1):
        new_list += l2[j:]
    return new_list

def recursive_merge_sort(list_to_be_sorted):
    final_list = []
    first = 0
    last = len(list_to_be_sorted)
    if last <= 1:
        final_list.extend( list_to_be_sorted )
    else:
        mid = last // 2
        l1 = recursive_merge_sort( list_to_be_sorted[:mid] )
        l2 = recursive_merge_sort( list_to_be_sorted[mid:] )
        final_list.extend( sort_and_merge( l1, l2 ) )
    return final_list

# Write a function to return the mean of numbers in a list
def cal_mean(num_list:list)->float:
    if num_list:
        return sum(num_list)/len(num_list)
    else:
        return None

# Write a function to return the median of numbers in a list
def cal_median(num_list:list)->float:
    if num_list:
        if len(num_list)%2 != 0:
            return sorted(num_list)[int(len(num_list)/2) - 1]
        else:
            return (sorted(num_list)[int(len(num_list)/2) - 1] + sorted(num_list)[int(len(num_list)/2)])/2
    else:
        return None

# Write a function to return the area of triangle by heros formula
def cal_triangle_area(a:float,b:float,c:float)->float:
    if a or b or c:
        s = (a+b+c)/2
        if s>a and s>b and s>c:
            area = (s*(s-a)*(s-b)*(s-c))**(1/2)
            return round(area,2)
        else:
            return None
    return None

# Write a function to return the area of a equilateral triangle
def cal_eq_triangle_area(a:float)->float:
    if a:
        return (3**(1/2))*(a**2)/4
    else:
        return None

# Write a function to return the area of a right angle triangle

def cal_rt_triangle_area(base:float,height:float)->float:
    if base and height:
        return (base*height)/2
    else:
        return None

# Write a function to return the cartisian distance of a point from origin
def cal_dist_from_orign(x:float,y:float)->float:
    return (x**2+y**2)**(1/2)

# Write a function to return the cartisian distance between two points
def cal_cart_distance(x1:float,y1:float,x2:float,y2:float)->float:
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

# Write a function to return the type roots of a quadratic equation ax**2 + bx + c = 0
def root_type(a:float,b:float,c:float):
    if b**2-4*a*c >= 0:
        return 'real'
    else:
        return 'imaginary'

# Write a function to return the sum of the roots of a quadratic equation ax**2 + bx + c = 0
def sum_of_roots(a:float,c:float):
    if a:
        return c/a
    else:
        return None

# Write a function to return the product of the roots of a quadratic equation ax**2 + bx + c = 0
def prod_of_roots(a:float,b:float):
    if a:
        return -b/a
    else:
        return None

# Write a function to return the real of the roots of a quadratic equation else return None ax**2 + bx + c = 0
def roots_of_qad_eq(a:float,b:float,c:float):
    d = b**2-4*a*c
    if d >= 0:
        return (-b+(d)**(1/2))/2*a,(-b-(d)**(1/2))/2*a
    else:
        return None

# Write a function to return the profit or loss based on cost price and selling price
def find_profit_or_loss(cp,sp):
    if cp > sp:
        return 'loss', cp-sp
    elif cp < sp:
        return 'profit', sp-cp
    else:
        return 'no profit or loss', 0

# Write a function to return the area of a rectangle
def cal_area_rect(length, breadth):
    return length*breadth

# Write a function to return the area of a square
def cal_area_square(side):
    return side**2

# Write a function to return the area of a rhombus with diagonals q1 and q2
def cal_area_rhombus(q1,q2):
    return (q1*q2)/2

# Write a function to return the area of a trapezium with base a base b and height h between parallel sides
def cal_area_trapezium(a,b,h):
    return h*(a+b)/2

# Write a function to return the area of a circle of raidus r
def cal_area_circle(r):
    pi = 3.14
    return pi*r**2

# Write a function to return the circumference of a circle
def cal_circumference(r):
    pi = 3.14
    return 2*pi*r

# Write a function to return the perimeter of a rectangle
def cal_perimeter_rect(length, bredth):
    return 2*(length+bredth)

# Write a function to return the perimeter of a triangle
def cal_perimeter_triangle(s1,s2,s3):
    return s1+s2+s3

# Write a function to return the perimeter of a square
def cal_perimeter_square(side):
    return 4*side

# Write a function to return the perimeter of an equilateral triangle
def cal_perimeter_eq_triangle(a):
    return 3*a

# Write a function to return the perimeter of a isoscales triangle
def cal_perimeter_iso_triangle(s1,s2):
    return 2*s1+s2

# Write a function to return the area of an ellipse
def cal_area_ellipse(minor, major):
    pi = 3.14
    return pi*(minor*major)

# Write a function to return the lateral surface area of a cylinder
def cal_cylinder_lat_surf_area(height,radius):
    pi=3.14
    return 2*pi*radius*height

# Write a function to return the curved surface area of a cone
def cal_cone_curved_surf_area(slant_height,radius):
    pi=3.14
    return pi*radius*slant_height

# Write a function to return the total surface area of a cube of side a
def cal_surface_area_cube(a):
    return 6*(a**2)

# Write a function to return the total surface area of a cuboid of length l, bredth b and height h
def cal_surface_area_cuboid(l,b,h):
    return 2*(l*b+b*h+h*l)

# Write a function to return the surface area of a sphere
def cal_area_sphere(radius):
    pi = 3.14
    return 4*pi*(radius**2)

# Write a function to return the surface area of a hemi-sphere
def cal_area_hemisphere(radius):
    pi = 3.14
    return 2*pi*(radius**2)

# Write a function to return the total surface area of a cylinder
def cal_cylinder_surf_area(height,radius):
    pi=3.14
    return 2*pi*radius**2*+2*pi*radius*height

# Write a function to return the lateral surface area of a cone
def cal_cone_lateral_surf_area(height,radius):
    pi=3.14
    return pi*radius*(((height**2)+(radius**2))**(1/2))

# Write a function to return the volume of a cylinder
def cal_cylinder_volume(height, radius):
    pi=3.14
    return pi*(radius**2)*height

# Write a function to return the volume of a cone
def cal_cone_volume(height,radius):
    pi=3.14
    return pi*(radius**2)*height/3

# Write a function to return the volume of a hemi sphere
def cal_hemisphere_volume(radius:float)->float:
    pi=3.14
    return (2/3)*pi*(radius**3)

# Write a function to return the volume of a sphere
def cal_sphere_volume(radius:float)->float:
    pi=3.14
    return (4/3)*pi*(radius**3)

# Write a function to return the volume of a cuboid
def cal_cuboid_volume(length:float, breadth:float, height:float)->float:
    return length*breadth*height

# Write a function to return the volume of a cube
def cal_cube_volume(side:float)->float:
    return side**3

# Write a function to return the speed of moving object based of distance travelled in given time
def cal_speed(distance:float,time:float)->float:
    return distance/time

# Write a function to return the distance covered by a moving object based on speend and given time
def cal_distance(time:float,speed:float)->float:
    return time*speed

# Write a function to return the time taken by a given of moving object based of distance travelled in given time
def cal_time(distance:float,speed:float)->float:
    return distance/speed

# Write a function to return the torque when a force f is applied at angle thea and distance for axis of rotation to place force applied is r
def cal_torque(force:float,theta:float,r:float)->float:
    import math
    return force*r*math.sin(theta)

# Write a function to return the angualr veolcity based on augualr distance travelled in radian unit and time taken
def cal_angular_velocity(angular_dist:float,time:float)->float:
    return angular_dist/time

# Write a function to calculate the focal length of a lense buy the distance of object and distance of image from lense
def cal_focal_length_of_lense(u:float,v:float)->float:
    return (u*v)/(u+v)

# Write a function to calculate the gravitational force between two objects of mass m1 and m2 and distance of r between them
def cal_gforce(mass1:float,mass2:float, distance:float)->float:
    g = 6.674*(10)**(-11)
    return (g*mass1*mass2)/(distance**2)

# Write a function to calculate the current in the curcit where the resistance is R and voltage is V
def cal_current(resistance:float, voltage:float)->float:
    return voltage/resistance

# Write a function to calculate the total capacitance of capacitors in parallel in a given list
def cal_total_cap_in_parallel(cap_list:list)->float:
    return sum(cap_list)

# Write a function to calculate the total resistance of resistances in parallel in a given list
def cal_total_res_in_parallel(res_list:list)->float:
    return sum([1/r for r in res_list])

# Write a function to calculate the total resistance of resistances in series in a given list
def cal_total_res_in_series(res_list:list)->float:
    return sum(res_list)

# Write a function to calculate the moment of inertia of a ring of mass M and radius R
def cal_mi_ring(mass:float,radius:float)->float:
    return mass*(radius**2)


# Write a function to calculate the moment of inertia of a sphere of mass M and radius R
def cal_mi_sphere(mass:float,radius:float)->float:
    return (7/5)*mass*(radius**2)


# Write a function to calculate the pressure P of ideal gas based on ideal gas equation - Volume V, and Temperatue T are given
def find_pressure_of_ideal_gas(volume:float, temp:float,n:float)->float:
    r = 8.3145 # gas constant R
    return (n*r*temp)/volume

# Write a function to calculate the volume V of ideal gas based on ideal gas equation Pressure P and Tempreature T given
def find_volume_of_ideal_gas(pressure:float, temp:float,n:float)->float:
    r = 8.3145 # gas constant R
    return (n*r*temp)/pressure

# Write a function to calculate the Temprature T of ideal gas based on ideal gas equation Pressure P and Volume V given

def find_temp_of_ideal_gas(pressure:float, volume:float,n:float)->float:
    r = 8.3145 # gas constant R
    return (pressure*volume)/n*r

# Write a function to calculate the velocity of an object with initial velocity u, time t and acceleration a
def cal_final_velocity(initial_velocity:float,accelration:float,time:float)->float:
    return initial_velocity + accelration*time

# Write a function to calculate the displacement of an object with initial velocity u, time t and acceleration a
def cal_displacement(initial_velocity:float,accelration:float,time:float)->float:
    return initial_velocity*time + .5*accelration*(time)**2

# Write a function to calculate amount of radioactive element left based on initial amount and half life
def cal_half_life(initail_quatity:float, time_elapsed:float, half_life:float)->float:
    return initail_quatity*((1/2)**(time_elapsed/half_life))

# Write a function to calculate the new selling price based on discount percentage
def cal_sp_after_discount(sp:float,discount:float)->float:
    return sp*(1 - discount/100)

# Write a function to calculate the simple interest for principal p, rate r and time in years y
def get_si(p:float, r:float, t:float)->float:
    return (p*r*t)/100

# Write a function to calculate the compound interest for principal p, rate r and time in years y
def get_ci(p:float, r:float, t:float, n:float)->float:
    return round(p*((1+(r/(n*100)))**(n*t)) - p,2)

# Write a function to calculate the energy released by converting mass m in kg to energy
def cal_energy_by_mass(mass:float)->float:
    c = 300000
    return mass * (c**2)

# Write a function to calculate the kinetic energy of an object of mass m and velocity v
def cal_ke(mass:float,velocity:float)->float:
    return (mass*(velocity)**2)/2

# Write a function to calculate the potential energy of an object of mass m at height h
def cal_pe(mass:float,height:float)->float:
    g = 9.8
    return (mass*g*height)

# Write a function to calculate the electrostatic force between two charged particles with charge q1 and q2 at a distance d apart
def cal_electrostatic_force(q1,q2,d):
    k = 9*(10**9)
    return (k*q1*q2)/(d**2)

# Write a function to calculate the density given mass and volume
def cal_density(mass,volume):
    return (mass/volume)

# Write a function to convert the temprature celsius 'c' to fahrenheit 'f' or fahrenheit to celsius
def temp_converter(temp,temp_given_in = 'f'):
    # Return the converted temprature
    if temp_given_in.lower() == 'f': # Convert to C
        return (temp - 32) * (5/9)
    else: # Convert to F
        return (temp * 9/5) + 32



# Write a function to merge dictionaries
def merge1():
    test_list1 = [{"a": 1, "b": 4}, {"c": 10, "d": 15},
                  {"f": "gfg"}]
    test_list2 = [{"e": 6}, {"f": 3, "fg": 10, "h": 1},
                  {"i": 10}]
    print("The original list 1 is : " + str(test_list1))
    print("The original list 2 is : " + str(test_list2))
    for idx in range(0, len(test_list1)):
        id_keys = list(test_list1[idx].keys())
        for key in test_list2[idx]:

            if key not in id_keys:
                test_list1[idx][key] = test_list2[idx][key]

    print("The Merged Dictionary list : " + str(test_list1))



# Write a function for vertical concatenating of a matrix
def vertical_concatenation():
    test_list = [["this","is"], ["program", "for"], ["vertical","concatenation"]]
    print("The original list : " + str(test_list))
    res = []
    N = 0
    while N != len(test_list):
        temp = ''
        for idx in test_list:
            try: temp = temp + idx[N]
            except IndexError: pass
        res.append(temp)
        N = N + 1
    res = [ele for ele in res if ele]
    print("List after column Concatenation : " + str(res))
vertical_concatenation()


# Write a function to Get Kth Column of Matrix
def kth_column(test_list=[[4, 5, 6], [8, 1, 10], [7, 12, 5]],k=2):

    print("The original list is : " + str(test_list))
    K =k
    res = list(zip(*test_list))[K]
    print("The Kth column of matrix is : " + str(res))

# Write a function to print all possible subarrays using recursion
def printSubArrays(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        return printSubArrays(arr, 0, end + 1)
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end)

arr = [1, 2, 3]
printSubArrays(arr, 0, 0)

# Write a function to find sum of nested list using Recursion
total = 0
def sum_nestedlist(l):
    global total
    for j in range(len(l)):
        if type(l[j]) == list:

            sum_nestedlist(l[j])
        else:
            total += l[j]

sum_nestedlist([[1, 2, 3], [4, [5, 6]], 7])
print(total)

#Write a function to find power of number using recursion
def power(N, P):
    if (P == 0 or P == 1):
        return N
    else:
        return (N * power(N, P - 1))

print(power(5, 2))


# Write a function to Filter String with substring at specific position
def f_substring():
    test_list = ['program ', 'to', 'filter', 'for', 'substring']
    print("The original list is : " + str(test_list))
    sub_str = 'geeks'
    i, j = 0, 5
    res = list(filter(lambda ele: ele[i: j] == sub_str, test_list))
    print("Filtered list : " + str(res))


# Write a function to remove punctuation from the string
def r_punc():
    test_str = "end, is best : for ! Nlp ;"
    print("The original string is : " + test_str)
    punc = r'!()-[]{};:\, <>./?@#$%^&*_~'
    for ele in test_str:
        if ele in punc:
            test_str = test_str.replace(ele, "")
    print("The string after punctuation filter : " + test_str)


# Write a function to implement Gnome Sort
def gnomeSort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr
arr = [34, 2, 10, -9]
n = len(arr)
arr = gnomeSort(arr, n)
print("Sorted seqquence after applying Gnome Sort :")
for i in arr:
    print(i)


# Write a function to implement Pigeonhole Sort */
def pigeonhole_sort(a):
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1
    holes = [0] * size
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
a = [8, 3, 2, 7, 4, 6, 8]
print("Sorted order is : ", end=" ")
pigeonhole_sort(a)
for i in range(0, len(a)):
    print(a[i], end=" ")



#Write a function to implement stooge sort
def stoogesort(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)
        stoogesort(arr, l, (h - t))
        stoogesort(arr, l + t, (h))
        stoogesort(arr, l, (h - t))

arr = [2, 4, 5, 3, 1]
n = len(arr)
stoogesort(arr, 0, n - 1)
for i in range(0, n):
    print(arr[i], end = '')

#Write a function to find the  difference between two times
def difference(h1, m1, h2, m2):

    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if (t1 == t2):
        print("Both are same times")
        return
    else:
        diff = t2 - t1
    h = (int(diff / 60)) % 24
    m = diff % 60
    print(h, ":", m)
difference(7, 20, 9, 45)
difference(15, 23, 18, 54)
difference(16, 20, 16, 20)


#Write a function to convert time from 12 hour to 24 hour format
def convert24(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]
print(convert24("08:05:45 PM"))


#Write a function to find time for a given angle.
def calcAngle(hh, mm):
    hour_angle = 0.5 * (hh * 60 + mm)
    minute_angle = 6 * mm
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    return angle


#Write a function to print all time when angle between hour hand and minute
def printTime(theta):
    for hh in range(0, 12):
        for mm in range(0, 60):
            if (calcAngle(hh, mm) == theta):
                print(hh, ":", mm, sep="")
                return
    print("Input angle not valid.")
    return
theta = 90.0
printTime(theta)