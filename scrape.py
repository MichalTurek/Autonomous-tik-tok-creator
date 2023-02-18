import random
import shutil, os
import requests
from bs4 import BeautifulSoup
import csv
import html2text
import urllib
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import cv2
from moviepy.editor import VideoFileClip

def get_vid_duration(filename):
    if(os.path.exists(filename)):
        clip = VideoFileClip(filename)
        print( clip.duration )
        clip.close()
        if(clip.duration <= 300.0):
            shutil.move(filename,'C:/Users/micha/OneDrive/Pulpit/GroupProject/GroupProject/videos/short/')
    
def scrape_page_products(url,driver,index):
    #downloader=urllib.FancyURLopener()
    
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    for product in soup.find_all("a", {"class": "video-item--a"}): 
        new_ulr = "https://rumble.com"+product['href']
        title = product.div.img['alt']
        #print(title)
        driver.get(new_ulr)
        req2 = requests.get(new_ulr)
        sauce = driver.page_source
        time.sleep(6)
        soup2 = BeautifulSoup(sauce,'html.parser')
        soup2.find()
        #soup2 = BeautifulSoup(req2.content, "html.parser")

        vid_url= soup2.find("video")['src']
        get_vid_duration(vid_url)
        #print(vid_url)
        urllib.request.urlretrieve(vid_url,"videos/tate_"+str(index)+".mp4")
        index = index+1
    return index

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    index=201

    for i in range(1,250):
        get_vid_duration("C:/Users/micha/OneDrive/Pulpit/GroupProject/GroupProject/videos/tate_"+str(i)+".mp4")
        #index = scrape_page_products("https://rumble.com/c/TateSpeech?page="+str(index),driver,index)
       

