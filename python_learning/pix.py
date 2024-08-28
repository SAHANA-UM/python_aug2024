def check_arrangement(boy_heigts, girl_heigts):
	arrangement_possible = True
	for i in range(1, len(boy_heigts)):
		if boy_heigts[i] < girl_heigts[i-1] or girl_heigts[i] < boy_heigts[i-1]:
			arrangement_possible = False
			break
	if arrangement_possible and ( (boy_heights[-1] > girl_heights[-2] and boy_heights[-1] > girl_heights[-1] ) or (girl_heights[-1] > boy_heights[-2] and girl_heights[-1] > boy_heights[-1] ) ):
		arrangement_possible = False
	if arrangement_possible:
		return 'Yes'
	return 'No'

T = int(input('Enter number of test cases: '))

arrangement = [] #stores yes/no 
n = 0
boy_heights = []
girl_heights = list()

for i in range(T):
	n = int(input('Enter number of boys/girls: '))
	print(f'Enter the heights of {n} boys')
	for i in range(n):
		boy_heights.append(int(input()))

	print(f'Enter the heights of {n} girls')
	for i in range(n):
		girl_heights.append(int(input()))
		
	boy_heights.sort()
	girl_heights.sort()
		
	arrangement.append( check_arrangement(boy_heights, girl_heights) )

print(arrangement)

    