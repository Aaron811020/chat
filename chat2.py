import os

#讀取檔案
def read_file(fileneme):
	chats = []
	with open(fileneme, "r", encoding = "utf-8-sig") as f:
		for line in f:
			chats.append(line.strip())	
	return chats

#文字轉換
def convert(chats):
	
	Allen_word_count = 0
	Allen_sticker_count = 0
	Allen_image_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_image_count = 0
	for line in chats:
		s = line.split(' ')
		time = s[0]
		name = s[1]

		if name == "Allen":
			if s[2] == "貼圖":
				Allen_sticker_count = Allen_sticker_count +1
			elif s[2] == "圖片":
				Allen_image_count = Allen_image_count +1
			else:
				for m in s[2:]:
					Allen_word_count = Allen_word_count + len(m)
		elif name == "Viki":
			if s[2] == "貼圖":
				Viki_sticker_count = Viki_sticker_count +1
			elif s[2] == "圖片":
				Viki_image_count = Viki_image_count +1
			else:
				for m in s[2:]:
					Viki_word_count = Viki_word_count + len(m)
	print("Allen 說了 %d 個字" %(Allen_word_count))
	print("Allen 傳了 %d 個貼圖" %(Allen_image_count))
	print("Allen 傳了 %d 個圖片" %(Allen_image_count))
	print("Viki %d 個字" %(Viki_word_count))
	print("Viki 傳了 %d 個貼圖" %(Viki_sticker_count))
	print("Viki 傳了 %d 個圖片" %(Viki_image_count))

#寫入檔案
def write_file(fileneme,chat):
	with open(fileneme, "w", encoding = "utf-8") as f:
		for line in chat:
			f.write(line+ "\n")

#主程式
def main():
	fileneme = input("請輸入來源檔案").strip()

	if os.path.isfile(fileneme):
		print("找到來源檔案")
		chats = read_file(fileneme)
		lines = convert(chats)

		#write_file('output.txt',lines)
	else:
		print("找不到來源檔案")

main()


