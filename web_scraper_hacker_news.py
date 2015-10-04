from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import time
import csv


def filterKeyword(articleObj, keyword):

	if (checkWordInSentence(articleObj.string, keyword)):
		title = articleObj.string
		link = articleObj.attrs['href']

		print ('---------')
		print (title)
		print (link)
		print ('\n')
		row = [title, link]
		c.writerow(row)


def checkWordInSentence (sentence, keyword):
	words = sentence.split()
	keyword = keyword.lower()
	for word in words:
		word=word.lower()
		if (word==keyword):
			return True
	return False

print ("Welcome to the HackerNews scraper")
keyword = input("Please type in a keyword you would like to filter links by: ")

c = csv.writer(open("results.csv", "w"), delimiter=',', dialect='excel')

for i in range(1, 500):
	start = str(i)
	print("Scraping page: "+str(start)+" of articles")
	url = "https://news.ycombinator.com/news?p="+start;
	html = urlopen(url)
	listingObj = BeautifulSoup(html.read(), "lxml")

	things = listingObj.findAll("tr", {"class":"athing"})

	for thing in things:
		artileObj = thing.find("span", {"class":"deadmark"}).next_sibling
		filterKeyword(artileObj, keyword)

	#time.sleep(30) #because hackernews.com/robots.txt defines crawl delay as 30 seconds