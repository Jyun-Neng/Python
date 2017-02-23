items = ["Lawrence", 1, "Ruby", 2, "Python", 3, "Java", 4, 5, 6, 7, 8, 9, 10]


def sort_list_num(items_list):
	num_items_list = [] # Store numbers
	
	for i in items_list:
		if isinstance(i, int):
			num_items_list.append(i)
		else:
			pass
	return num_items_list

def sort_list_str(items_list):
	str_items_list = []	# Store string

	for i in items_list:
		if isinstance(i, str):
			str_items_list.append(i)
		else:
			pass
	return str_items_list

def sum_of_list(items_list):
	num_list = sort_list_num(items)
	total = sum(num_list)
	return total

def average(items_list):
	total = sum_of_list(items_list)
	num = len(sort_list_num(items_list))
	ave = total / num
	return ave


sum_of_items = sum_of_list(items)
ave_of_items = average(items)
num_list = sort_list_num(items)
str_list = sort_list_str(items)

print("the numbers in the items are ", sort_list_num(items))
print("the strings in the items are ", sort_list_str(items))
print("the sum of the numbers in the items is ", sum_of_items)
print("the average of the numbers in the items is ", ave_of_items)