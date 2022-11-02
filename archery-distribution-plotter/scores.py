# imports
# pandas for opening csv, setting up and manipulating a dataframe
# seaborn and matplotlib for plotting and grpah formatting
# tkinter.filedialog for setting file directory of inout csv file
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tkinter import filedialog as fd

# tkinter.filedialog
# opens a file explorer instance allowing the user to set the path
# to the input csv file
input_file = fd.askopenfilename()

# pandas reads the input file, saving the dataframe as df
# delimiter semicolon ;
df = pd.read_csv(input_file,sep=";")
# removes speech marks
df.replace("\"","")
# creates a new columns called "neg_y" with the sign flipped values of y
# MyTargets outputs the y values as negative for some reason 
df["neg_y"] = df["y"] * -1
# creates a new columns  called "index" which corresponds to the arrow number
# this is used in the title to display the sample size
df["index"] = [i+1 for i in range(len(df))]

# saves Date, Standard round and index into lists
date = df.Date
round = df["Standard round"]
arrow = df["index"]
# Formats the title with the first values of round and date and the last
# value of arrow (index)
title = f"{round[0]} on {date[0]}: N={arrow[len(arrow)-1]}\n"

# plots a joint plot showing the distribution of arrows
sns.set_theme(style="darkgrid")
ax = sns.jointplot(data=df,x="x",y="neg_y",kind="kde",fill=True)

# Sets the plot title and title location
plt.title(title, y=-0.05)
# Sets the x and y axis labels
plt.xlabel("Windage")
plt.ylabel("Elevation")

# Sets the scope/range of the plot
plt.ylim(-1, 1)
plt.xlim(-1, 1)
# Creates a reference line at x=0 and y=0, where these meet is bullseye
ax.refline(x=0, y=0)

# Circles to represent the different point values on the graph
# not perfect as these circles move with the scale of the plot
# this is because matplotlib is a plotting module, not drawing so it has no good
# way to display reference circles :)
# circles are overlayed on top of the figure rather than intrinsically PART OF
# the plot
# this is okay at the default size with a 1:1 height width ratio however if the 
# user was to resize the window then the data would be skewed with respect to
# the circles
ax.ax_joint.plot([0],[0],'o',ms=15,mec='gold',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=60,mec='gold',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=90,mec='red',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=120,mec='red',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=150,mec='DeepSkyBlue',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=180,mec='DeepSkyBlue',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=210,mec='black',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=240,mec='black',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=270,mec='white',mfc='none')
ax.ax_joint.plot([0],[0],'o',ms=300,mec='white',mfc='none')
plt.show()
