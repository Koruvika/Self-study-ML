import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

data = pd.read_csv("StudentsPerformance.csv")

parental_level_of_education = data["parental level of education"].unique()
gender = data["gender"].unique()
test_preparation_course = data["test preparation course"].unique()
lunch = data["lunch"].unique()

def addText(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2, height+1,int(height), ha="center", va="bottom")
        
        
plt.style.use("seaborn")

plt.rcParams["legend.edgecolor"] = "red"
fig, ax = plt.subplots(ncols=2, nrows=2, figsize = (18, 12))
fig.tight_layout()
# sns.set_style("darkgrid") 
fig.subplots_adjust(wspace=0.1, hspace=0.15)
# ax 0 0
math_score = []
reading_score = []
writing_score = []
for level in parental_level_of_education:
    math_score.append(np.average(np.array(data.loc[(data["parental level of education"] == level)]["math score"])))
    reading_score.append(np.average(np.array(data.loc[(data["parental level of education"] == level)]["reading score"])))
    writing_score.append(np.average(np.array(data.loc[(data["parental level of education"] == level)]["writing score"])))


idx = np.arange(len(parental_level_of_education))
ax[0,0].set_xticks(idx)
ax[0,0].set_xticklabels(parental_level_of_education, fontsize = 12)
ax[0,0].set_ylabel('Scores')
ax[0,0].set_title("Score Comparison by Parental Level of Education", fontdict={'fontsize': 24})
rects1 = ax[0,0].bar(idx-0.25, math_score, 0.25, label="Math")
rects2 = ax[0,0].bar(idx, reading_score, 0.25, label="Reading")
rects3 = ax[0,0].bar(idx+0.25, writing_score, 0.25, label="Writing")

ax[0,0].margins(0.15,0.08)
ax[0,0].legend()

# ax 0 1
math_score = []
reading_score = []
writing_score = []
for level in gender:
    math_score.append(np.average(np.array(data.loc[(data["gender"] == level)]["math score"])))
    reading_score.append(np.average(np.array(data.loc[(data["gender"] == level)]["reading score"])))
    writing_score.append(np.average(np.array(data.loc[(data["gender"] == level)]["writing score"])))
    
idx = np.arange(len(gender))

ax[0,1].set_xticks(idx)
ax[0,1].set_xticklabels(gender, fontsize = 12)
ax[0,1].set_ylabel('Scores')
ax[0,1].set_title("Score Comparison by Gender", fontdict={'fontsize': 24})
rects4 = ax[0,1].bar(idx-0.25, math_score, 0.22, label="Math")
rects5 = ax[0,1].bar(idx, reading_score, 0.22, label="Reading")
rects6 = ax[0,1].bar(idx+0.25, writing_score, 0.22, label="Writing")

ax[0,1].margins(0.15,0.08)
ax[0,1].legend()

# ax 1 0
math_score = []
reading_score = []
writing_score = []
for level in test_preparation_course:
    math_score.append(np.average(np.array(data.loc[(data["test preparation course"] == level)]["math score"])))
    reading_score.append(np.average(np.array(data.loc[(data["test preparation course"] == level)]["reading score"])))
    writing_score.append(np.average(np.array(data.loc[(data["test preparation course"] == level)]["writing score"])))
    
idx = np.arange(len(test_preparation_course))

ax[1,0].set_xticks(idx)
ax[1,0].set_xticklabels(test_preparation_course, fontsize = 12)
ax[1,0].set_ylabel('Scores')
ax[1,0].set_title("Score Comparison by Test Preparation Course", fontdict={'fontsize': 24})
rects7 = ax[1,0].bar(idx-0.25, math_score, 0.22, label="Math")
rects8 = ax[1,0].bar(idx, reading_score, 0.22, label="Reading")
rects9 = ax[1,0].bar(idx+0.25, writing_score, 0.22, label="Writing")

ax[1,0].margins(0.18,0.08)
ax[1,0].legend();

# ax 1 1
math_score = []
reading_score = []
writing_score = []
for level in lunch:
    math_score.append(np.average(np.array(data.loc[(data["lunch"] == level)]["math score"])))
    reading_score.append(np.average(np.array(data.loc[(data["lunch"] == level)]["reading score"])))
    writing_score.append(np.average(np.array(data.loc[(data["lunch"] == level)]["writing score"])))
    
idx = np.arange(len(lunch))
ax[1,1].set_xticks(idx)
ax[1,1].set_xticklabels(lunch, fontsize = 12)
ax[1,1].set_ylabel('Scores')
ax[1,1].set_title("Score Comparison by Lunch", fontdict={'fontsize': 24})
rects10 = ax[1,1].bar(idx-0.25, math_score, 0.22, label="Math")
rects11 = ax[1,1].bar(idx, reading_score, 0.22, label="Reading")
rects12 = ax[1,1].bar(idx+0.25, writing_score, 0.22, label="Writing")
ax[1,1].margins(0.15,0.08)
ax[1,1].legend();       

addText(rects1, ax[0,0])
addText(rects2, ax[0,0])
addText(rects3, ax[0,0])
addText(rects4, ax[0,1])
addText(rects5, ax[0,1])
addText(rects6, ax[0,1])
addText(rects7, ax[1,0])
addText(rects8, ax[1,0])
addText(rects9, ax[1,0])
addText(rects10, ax[1,1])
addText(rects11, ax[1,1])
addText(rects12, ax[1,1])