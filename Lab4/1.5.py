sample_input = (55, 6, 777, 70.0, '7', 'A')


result_tuples = []
current_tuple = ()


for item in sample_input:
    if isinstance(item, (int, float)):
        
        current_tuple += (item,)
    else:
        if current_tuple:
            result_tuples.append(current_tuple)
            current_tuple = ()  #

if current_tuple:
    result_tuples.append(current_tuple)

for t in result_tuples:
    print(t)
