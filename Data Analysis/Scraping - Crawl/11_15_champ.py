# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 14:13:36 2021

@author: Admin
"""

from selenium import webdriver
from time import sleep
import pandas as pd
import matplotlib.pyplot as plt

# Definition form of data

champs_list = []
# =============================================================================
# champ = [Ten, Cost, Toc, He, Health, Attack Damage, DPS, Attack Range, Attack Speed,
#          Armor & Magical Resistance, Skill Name, Mana Cost, Skill Description]
# =============================================================================

# Open Browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://lolchess.gg/champions/set5.5/"
browser.get(url)
sleep(2)

# Find Urls
champ_boxs = browser.find_elements_by_css_selector("a.guide-champion-list__item")
champ_box_urls = []
for champ_box in champ_boxs:
    champ_box_urls.append(champ_box.get_attribute("href"))
    
# Function to get data
def getData(url) :
    browser.get(url)
    sleep(0.5)
    champ = []
    name = browser.find_element_by_css_selector("span.guide-champion-detail__name").text
    champ.append(name)
    # cost = browser.find_element_by_css_selector("div.guide-champion-detail__stats__value").text
    stats = browser.find_elements_by_css_selector("div.guide-champion-detail__stats__row")
    cost = stats[0].find_element_by_css_selector("div.guide-champion-detail__stats__value").text.strip()[0]
    champ.append(cost)
    
    toc = ""
    he = ""
    toc_list = stats[1].find_elements_by_tag_name("img")
    for race in toc_list:
        toc = toc + race.get_attribute("alt") + ";"
    
    he_list = stats[2].find_elements_by_tag_name("img")
    for gen in he_list:
        he = he + gen.get_attribute("alt") + ";"
    champ.append(toc)
    champ.append(he)
    
    base_stats = browser.find_elements_by_css_selector("div.guide-champion-detail__base-stat__value")
    exs = browser.find_elements_by_class_name("font-size-11.text-light-gray.d-lg-none")
    
    health = base_stats[0].text.strip()
    health = health[0:health.rfind(exs[0].text.strip())]
    champ.append(health)
    atk = base_stats[1].text.strip()
    atk = atk[0:atk.rfind(exs[1].text.strip())]
    champ.append(atk)
    dps = base_stats[2].text.strip()
    dps = dps[0:dps.rfind(exs[2].text.strip())]
    champ.append(dps)                    
    
    src = base_stats[3].find_element_by_tag_name("img").get_attribute("src")
    range_atk = 1
    if src == "//cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance302.png" :
        range_atk = 2
    if src == "//cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance303.png" :
        range_atk = 3
    if src == "//cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance304.png" :
        range_atk = 4
    if src == "//cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance305.png" :
        range_atk = 5
    champ.append(range_atk)
    speed_atk = base_stats[4].text.strip()
    champ.append(speed_atk)
    armor = base_stats[5].text.strip()
    champ.append(armor)
    champ.append(armor)
    
    skill_box = browser.find_element_by_css_selector("div.guide-champion-detail__skill")
    name_skill = skill_box.find_element_by_tag_name("strong").text.strip()
    champ.append(name_skill)
    mana_cost = skill_box.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[6]/div/div[3]/div/div[4]/div[1]/span[3]').text[5:].strip()
    champ.append(mana_cost)
    skill_des = skill_box.find_element_by_css_selector("span.d-block.mt-1").text.strip()
    skill_des = skill_des + skill_box.find_element_by_css_selector("div.guide-champion-detail__skill__stats").text.strip()
    champ.append(skill_des)
    champs_list.append(champ)
    
    
for champ_box_url in champ_box_urls:
    getData(champ_box_url)
    
# Close browser
sleep(2)
browser.close()

df = pd.DataFrame(champs_list, columns=["Name", "Cost", "Race", "Generation", "Health", "Attack Damage", "DPS", "Attack Range", "Attack Speed", "Armor ", "Magical Resistance", "Skill Name", "Mana Cost", "Skill Description"])
df.to_csv("champs_5d5.csv")