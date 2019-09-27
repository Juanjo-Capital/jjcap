#https://www.stockmonitor.com/sector/technology/

'''outputs a list of tech companies with volume less than 1 billion'''
def getCompany(s, retList):
    list = s.split("\t")
    name = list[1]
    volume = list[4]
    if int(volume.replace(',',''))<1000000:
        retList.append(str(name)+'\n')

file = open('techCompanies.txt','r');
finalList = []
for line in file:
    getCompany(line, finalList)
file.close()

'''write this to a new file'''
file2 = open('finalTechCompanies.txt','w')
file2.writelines(finalList)

for company in finalList:
    print(company)