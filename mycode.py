import codecs
def lines(poems):
	result = {}
	with open(poems, "r", encoding='utf-8') as file:
		line = file.readlines()
		for i in range(len(line)):
			if "Автор" in line[i]:
				author = line[i].replace("Автор: ", "").replace("\n", "")
				name = line[i+1].replace("Назва: ", "").replace("\n", "")
				first_line = line[i+2].replace("\n", "")
				result[name] = {"Author": author, "first_line": first_line}
	return result



print(lines("poems.txt"))
