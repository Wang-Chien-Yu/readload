#讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		#if count % 1000 == 0: # %求餘數
			#print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d) 
	#將每筆留言的字數存起來到sum_len
print('每筆留言平均長度為: ', sum_len/len(data))
