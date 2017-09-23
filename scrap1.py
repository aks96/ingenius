import requests
from bs4 import BeautifulSoup
# def amazon():
url="https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=shirts"
# https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=pants
r=requests.get(url)

soup = BeautifulSoup(r.content,"lxml")
links = soup.find_all("li",{"class" : "s-result-item"})

amazonData = []

i = 0
print len(links)
for link in links:
			#print "<a href='%s'>%s</a>"%(link.get("href",link.text)
	# print link.get("id")
	i=i+1
	if i == 5:
		break
	temp = []
	try:
		g_data = link.find("h2")
		temp.append(g_data.text)
	except:
		pass 
	try:
		price = link.find("span", {"class" : "s-price"})
		temp.append(price.text)
	except:
		pass 
	try:
		stars = link.find("a", {"class" : "a-popover-trigger"}).find("span", {"class" :""})
		temp.append(stars.text)
	except:
		temp.append("0")
	try:
		ratings = link.find_all("a", {"class" : "a-link-normal"})
		temp.append(ratings[len(ratings)-1].text)
	except:
		temp.append("0")

	amazonData.append(temp)

print "--------------------------------\nAMAZON\n---------------------------------"
print amazonData
print "------------------------------------------------------------------\n\n\n"

url="https://www.flipkart.com/mens-footwear/sports-shoes/pr?sid=osp,cil,1cu&otracker=nmenu_sub_Men_0_Sports%20Shoes"
r=requests.get(url)

flipkartData = []

soup = BeautifulSoup(r.content,"lxml")
links = soup.find_all("div",{"class" : "_3yI_5w"})
i = 0
print len(links)
for link in links:
	temp = []
	i=i+1;
	if(i==5):
		break
	# print link.get("div")
	try:
		g_data = link.find("div",{"class" : "_3liAhj"}).find("a",{"class" : "_2cLu-l"})
		temp.append(g_data.text)
	except:
		pass
	try:
		price = link.find("div", {"class" : "col"}).find("div",{"class" : "_1uv9Cb"}).find("div",{"class" : "_1vC4OE"})
		temp.append(price.text)
	except:
		pass
	try:
		stars = link.find("div", {"class" : "col"}).find("div",{"class" : "niH0FQ"}).find("span", {"class" :"_2_KrJI"})
		temp.append(stars.text)
	except:
		temp.append("0")
	try:
		ratings = link.find("div",{"class" : "col"}).find("div", {"class" : "niH0FQ"}).find("span",{"class" : "_38sUEc"})
	# print ratings[len(ratings)-1].text
		temp.append(ratings.text)
	except:
		temp.append("0")
		pass
	flipkartData.append(temp);


print "--------------------------------\nFLIPKART\n---------------------------------"
print flipkartData
print "------------------------------------------------------------------"



newData = []
for d in amazonData:
	temp = d
	print "--------------------"
	print "Name : "+ (d[0])
	print "Price : " + (d[1])
	print "Stars : " + (d[2])
	try:
		print "Ratings : " + (d[3])
	except:
		print "Ratings : " + str(0)

	score = "123"
	temp.append(score)
	print "--------------------"
	newData.append(temp);

print newData