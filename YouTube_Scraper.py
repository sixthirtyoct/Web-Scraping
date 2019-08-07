import os
from bs4 import BeautifulSoup
import requests
import csv

query=input("Enter: ")
query="+".join(query.split())
source=requests.get("https://youtube.com/results?search_query="+query).text
soup=BeautifulSoup(source,'lxml')

title,duration,views,posted,uploader,link=[None]*6

csv_file=open('ScrapedFile.csv','w')

writer=csv.writer(csv_file)

writer.writerow(["Title","Duration","Views","Posted","Uploader","Link"])

'''
Things i want
1.) Name of the video
2.) Duration
3.) Views
4.) Posted
5.) Uploader
6.) Video Link
'''

for match in soup.find_all('div',class_="yt-lockup-content"):
    try:

        info1=match.find('a',class_="yt-uix-tile-link")
        title=info1['title'].strip()
        #print("Title:",title)

        info2=match.find('span',class_="accessible-description")
        duration=info2.text.strip().replace("- Duration: ","")[:-1]
        #print("Duration:",duration)


        info3=match.find('div',class_="yt-lockup-meta")
        info3=info3.text.split("ago")
        posted=info3[0].strip()
        views=info3[-1].strip()

        #print("Views:",views)
        #print("Time:",posted)

        info5=match.find('div',class_="yt-lockup-byline")
        uploader=info5.text.strip()
        #print("Uploader:",uploader)


        link="https://youtube.com"+info1['href']
        #print("Link:",link)
        #print("*"*30)
        #print()


    except Exception:
        title="Playlist"
        duration,views,posted,uploader,link=[None]*5

    writer.writerow([title,duration,views,posted,uploader,link])

print("Successfully Done!")
csv_file.close()
