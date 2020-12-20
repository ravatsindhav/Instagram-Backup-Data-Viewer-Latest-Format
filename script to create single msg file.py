import json
import os

file_arr = [os.path.join(r,file) for r,d,f in os.walk(".") for file in f if file.endswith(".json")]
print(file_arr)
resultList = []
for filePath in file_arr:

	with open(filePath,encoding="utf8") as f:
		data = json.load(f)

	#print(data)
	
	resultList.append(data)

result = json.dumps(resultList)
with open('messages.json', 'a') as json_file:
	json_file.write(result)


#print([os.path.join(r,file) for r,d,f in os.walk(".") for file in f if file.endswith(".json")])  
	
	