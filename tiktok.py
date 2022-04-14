from selenium import webdriver
from utils import wait
from credentials import TIKTOK_USER

# mass follow+unfollow
URL = 'https://www.tiktok.com'
PROFILE = URL + f'/@{TIKTOK_USER}?lang=en'

class TikTokBot():
    def __init__(self, username):
        self.username = username
        self.bot = webdriver.Chrome()


    def login(self):
        self.bot.get(URL)
        ele_list = len(self.bot.find_elements_by_class_name('message-icon'))
        while ele_list == 0:
            print("---------- WAITING FOR LOGIN ----------")
            wait()
            l = len(self.bot.find_elements_by_class_name('message-icon'))
            ele_list = l
        print("---------- LOGIN SUCCESSFUL ----------")
        wait()
 
            
    def navigate_to_profile(self):
        bot = self.bot
        bot.get(PROFILE)
        wait()


    def remove_bad_followers(self):
        print("navigating to profile...")
        wait()
        self.navigate_to_profile()
        bot = self.bot

        # followers
        followers_btn = bot.find_elements_by_class_name('header-inbox-icon')[0]
        followers_btn.click()

        followers_tab = bot.find_elements_by_class_name('group-wrap')[0] \
            .find_elements_by_tag_name('span')[4]
        followers_tab.click()

        followers = [
            u.get_attribute("textContent").split(" ")[0]
            for u in bot.find_elements_by_class_name('notice-list')[0] \
                .find_elements_by_class_name('notification-item')
        ] 

        has_follows = True        
        try:
            following_list = [
                {
                    "name": u.get_attribute("textContent").split(" ")[0],
                    "url": u.get_attribute("href")
                }
                for u in bot.find_elements_by_class_name('user-list')[0] \
                    .find_elements_by_tag_name('a')
            ]
        except IndexError:
            has_follows = False
            print("---------- you dont have any follows ----------")

        # remove
        if has_follows:
            self.remove_follows_execute(following_list, followers)
    
    
    def remove_follows_execute(self, following_list, followers):
        count = 120
        bot = self.bot
        for u in following_list:
            follower_is_good = False

            for e in followers:
                if e == u["name"]:
                    follower_is_good = True

            if not follower_is_good and count < 120:
                u_profile = u["url"]
                bot.get(u_profile)
                wait()
                wait()

                bot.find_elements_by_class_name('icon-follow')[0].click()
                wait()
                count+=1

                bot.get(PROFILE)
                wait()
                wait()
            else:
                bot.get(PROFILE)
                wait()
                wait()


user = TikTokBot(TIKTOK_USER)
user.login()
wait()
user.remove_bad_followers()
print('---------- DONE ----------')
