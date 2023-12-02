
textList = [] 
file = open("input.txt", "r")
while True:
	content=file.readline()
	if not content:
		break
	textList.append(content)
file.close()

totalSum = 0
for word in textList:
	allDigits = ""
	calibrationValues = ""
	for letter in word:
		if letter.isdigit():
			allDigits += letter
	calibrationValues += allDigits[0]
	calibrationValues += allDigits[len(allDigits) - 1]
	totalSum += int(calibrationValues)
	
print(totalSum)

