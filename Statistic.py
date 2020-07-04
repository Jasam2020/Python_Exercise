from statistics import mode
n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)
print("Minimum:" + str(min(n_num)))
print("Maximum:" + str(max(n_num)))
print("Mode:" + str(mode(n_num)))
get_sum = sum(n_num)
mean = get_sum / n
print("Mean / Average is: " + str(mean))
median = n_num[n//2]
print("Median is: " + str(median))

