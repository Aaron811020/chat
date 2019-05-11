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
	name = None
	new = []
	for line in chats:
		if "Allen" in line or "Tom" in line:
			name = line
			continue
		if name:
			new.append(name + ":" + line)
	return new


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
		print(chats)
		lines = convert(chats)
		print(lines)
		write_file('output.txt',lines)
	else:
		print("找不到來源檔案")

main()


