
red=2567.9
blue=18934.9
green=678.98
yellow=456.2
orange=50
lst=[red,blue,green,yellow,orange]
players=["RED","BLUE","GREEN","YELLOW","ORANGE"]


order=[]


def arrange(order,lst):
	for i in range(0,5):
		for j in range(0,4):
			if(lst[i]<lst[j]):
				temp=lst[i]
				lst[i]=lst[j]
				lst[j]=temp

	for i in range(0,5):
		if red==lst[i]:
			order.append("RED")

		if blue==lst[i]:
                	order.append("BLUE")

		if green==lst[i]:
                	order.append("GREEN")

		if orange==lst[i]:
                	order.append("ORANGE")

		if yellow==lst[i]:
                	order.append("YELLOW")

	return order,lst


order,lst=arrange(order,lst)
print order
print lst

