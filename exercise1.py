import readline
import sys
import statistics

with open(sys.argv[1], 'r') as file:
    contents = file.readlines()
    
    total = 0
    line_count = 0
    list_num = []
    for number in contents:
        total+= int(number)
        list_num.append(number)
        line_count+=1
    
    mean = total/line_count
    std = statistics.stdev(list_num)
    min = min(list_num)
    max = max(list_num)

print("Statistics summary")
print(f"Mean: {mean}")
print(f"Std: {std}")
print(f"Min: {min}")
print(f"Max: {max}")