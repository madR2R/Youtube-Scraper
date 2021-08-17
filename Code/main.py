#Selenium Imports
import os
import time
from colorama.ansi import Fore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#WebHook
from discord_webhook import DiscordWebhook, DiscordEmbed

#Disabling Notification
os.system('cls')

def scrapeYoutubeChannel():
    PATH = 'E:\Softwares\ChromeDriver\chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    #Saving informations
    global links, images, vidTitles, objects
    links = []
    images = []
    vidTitles = []

    #User must input Youtube channel
    print(Fore.YELLOW+ 'Input Youtube Channel Link! \n'+Fore.CYAN+'Example here: https://www.youtube.com/c/EROVOUTIKARoboticsandAutomationSolutions/videos ')
    channelName = input(Fore.WHITE+'Please Enter Youtube channel link: ')
    driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
    driver.get(channelName)

    
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #target anchors
    anchors = driver.find_elements_by_tag_name('a') 
    for a in anchors:
        attr = a.get_attribute('href')
        if str(attr).startswith('https://www.youtube.com/watch?v'):
           links.append(attr)

    #Avoid Duplicate links
    links = list(dict.fromkeys(links))
    
    image = driver.find_elements_by_tag_name('img')
    for i in image:
        attr = i.get_attribute('src')
        if str(attr).startswith('https://i.ytimg.com/'):
            images.append(attr)

    titles = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for title in titles:
        vidTitles.append(title.text)
    
    objects = {
        'ytLinks': links,
        'titleVid': vidTitles,
        'images' : images
    }
    
    ytVidLinks = open('ytVidLinks.txt', 'a+')

    #Saving latest video uploaded
    latestUpload = open('latestUpload.txt', 'w')
    latestUpload.write(objects['ytLinks'][0])

    #Saving youtube video links
    counter = 0
    for a in objects['ytLinks']:
        ytVidLinks.write(objects['titleVid'][counter]+"\n"+objects['ytLinks'][counter]+"\n")
        counter += 1
    driver.quit()

def playVideo():

    #Check if the text file is empty
    filesize = os.path.getsize("ytVidLinks.txt")
    if filesize == 0:
        print(Fore.RED+"List is empty! Please scrape first!")
    else:
        with open('ytVidLinks.txt', 'r') as vidLists:
            #Save title and links
            list = []
            title = []
            links = []

            #Save to lists
            count = 1
            for line in vidLists:
                strippedLine = line.strip()
                list.append(strippedLine)

        #Show video titles and links
        length = len(list)
        for i in range(length):
            if i%2 == 0:
                title.append(list[i])
            elif i%2 != 0:
                links.append(list[i])

        #Selection
        count = 0
        for title in title:
            print("[{}] : {}".format(count, title))
            count += 1
        
        #Select a Video to play
        choice = input('Please Select: ')

        #Open the video and input additional chrome options
        PATH = 'E:\Softwares\ChromeDriver\chromedriver.exe'
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--kiosk")
        driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
        driver.get(links[int(choice)])
        

def main():
    scrapeYoutubeChannel()
    playVideo()

if __name__ == '__main__':
    main()