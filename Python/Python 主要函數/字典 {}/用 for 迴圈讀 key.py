info={ "ABC":"123", "name":"yiru", "phone":"091123456", "add":"taipei" } 

for forkey in info: 

	print("欄位為:",forkey) 
	#第1圈 abc 、第2圈 name、第3圈 phone 、第4圈 add 
	print("值為:",info[forkey]) 
	#第1圈 info[abc] 、第2圈 info[name]、第3圈 info[phone] 、第4圈 info[add] 
	print("=================")