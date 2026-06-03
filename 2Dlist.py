#2D list(kind of matrix with rows and columns)
#list made of a list(useful when we need grade or matrix related data)

#eg:
num_pad=(( 1, 2, 3),
         ( 4, 5, 6),
         ( 7, 8, 9),
         ( "*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
    
