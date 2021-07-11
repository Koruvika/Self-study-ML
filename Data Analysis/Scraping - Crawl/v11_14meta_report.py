from selenium import webdriver
from time import sleep
import pandas as pd

browser = webdriver.Chrome(executable_path="./chromedriver.exe")


# mo trinh duyet
url = "https://lolchess.gg/meta"
browser.get(url)
sleep(3)
# click button to show name
showname_button = browser.find_element_by_id("toggle-meta-show-name")
showname_button.click()
sleep(2)

# 
team_comp_divs = browser.find_elements_by_class_name("guide-meta__deck")
team_comps = []
for div in team_comp_divs:
    name_comp = div.find_element_by_class_name("guide-meta__deck__column.name.mr-3").text
    name_champs = ""
    champs_div = div.find_elements_by_class_name("tft-champion-box")
    for champ_box in champs_div:
        name_champ = champ_box.find_element_by_class_name("name").text
        name_champs = name_champs + name_champ + ";"
    cost_comp = div.find_element_by_css_selector("span.d-block").text
    team_comp = [name_comp, name_champs, cost_comp]
    team_comps.append(team_comp)

# Close browser
sleep(2)
browser.close()

# Save data
df = pd.DataFrame(team_comps, columns=["name", "champs", "cost"])
df.to_csv("meta__v11_14.csv")