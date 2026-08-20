temprature = [32.3, 32.4, 32.5, 32.6, 32.7]
total =0
for temp in temprature:
    total += temp

average = total/len(temprature)
print("Average temprature is:",average)