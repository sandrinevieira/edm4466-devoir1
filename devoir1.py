#coding : utf-8

urlList = []

for number in range(20000,30151):
    
    urlList.append("https://montrealcampus.ca?p=" + str(number))

print("Voici la liste des URLs: ")
print(urlList)
print("Nombre Total de URLs:")
print(len(urlList))

