tuple1 = ('ab', 78)
tuple2 = (99, 'cd')
print(f'From the original Tuple 1 = {tuple1}','\n',f'\t   and Tuple2 = {tuple2} \nThe newly swapped tuples are:' )
tuple1,tuple2=tuple2,tuple1
print(f'Tuple 1 = {tuple1}')
print(f'Tuple 2 = {tuple2}')