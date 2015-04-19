#--------------------------------------------------
#--------------------------------------------------
# Name:   GeeksForGeeks Article Extractor
# Purpose: To download and save articles filed under each and every tag mentioned in www.geeksforgeeks.org 
# developed by Aryak Sengupta(@aryak93) and modified by Prabhanshu Attri (@nirmankarta)
#--------------------------------------------------
#--------------------------------------------------

from bs4 import BeautifulSoup
import urllib2
import os.path

AllTags = ['interview-experience','advance-data-structures','dynamic-programming','Greedy-Algorithm','backtracking','pattern-searching','divide-and-conquer','graph','MathematicalAlgo','recursion','Java']

path = ""      # Specify your path here
#path = "E:\GeeksForGeeks\\" 	#Sample windows path
#path = "/home/nirmankarta/" 	#Sample windows path

def ExtractMainLinks(AllTags,path):
	print '\n\nGeeksforGeeks Website extracter'
	print '-------------------------------------------------------------------------------------'
	print 'developed by Aryak Sengupta(@aryak93) and modified by Prabhanshu Attri (@nirmankarta)'
	print '-------------------------------------------------------------------------------------'
	n = 0
	for i in AllTags:		
		url = "http://www.geeksforgeeks.org/tag/" + i +"/"
		print '\nRetrieving tag {0} of {1}: {2}'.format(n+1,len(AllTags),i)
		data = urllib2.urlopen(url).read()
		soup = BeautifulSoup(data)
		allLinks = soup.findAll("h2",class_="post-title")
		listofLinks = []
		for link in allLinks:
			mainLink = str(link.findAll("a")[0]).split("<a href=")[1].split('rel="bookmark"')[0].strip('"').split('"')[0]
			listofLinks.append(mainLink)
		Extract_And_Save_Page_Data(listofLinks,path,i)
		n = n + 1
		
def Extract_And_Save_Page_Data(listofLinks,path,i):
	No = 0
	if not os.path.exists(path+i):
		os.mkdir(path+i)
	for item in listofLinks:
		pageData = urllib2.urlopen(item).read()
		pageName = item.replace("http://www.geeksforgeeks.org/", "");
		pageName = pageName[:-1]
		pageName = pageName+".html"
		filePath = path + i[0:] +"/" +pageName
		No = No +1
		if os.path.isfile(filePath):
			print '\t{0} of {1}: {2} is exists!'.format(No, len(listofLinks), pageName)
		else:
			with open(filePath,"wb") as f:
				f.write(str(pageData))		
			print '\t{0} of {1}: {2} is saved!'.format(No, len(listofLinks), pageName)

ExtractMainLinks(AllTags,path)
