import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tkinter import filedialog as fd
import os

# set input csv file and output directory using tkinters filedialog
input_file = fd.askopenfilename(filetypes=[("CSV files", "*.csv")],title="Set input .csv file")
output_dir = fd.askdirectory(title="Set output folder (plots will be saved here)")

# pandas read the csv and sanitise it for use
# the sign for "y" is flipped as the input data is w r o n g
df = pd.read_csv(input_file,sep=";")
df.replace("\"","")
df["neg_y"] = df["y"] * -1

sns.set_theme(style="darkgrid",palette="pastel")

# creates two lists called "sizes" and "flattened_colours" (1d) and returns them
# these lists are then used in func:plot_target_face_and_ref_line
def set_size_and_colour_list():
    sizes = [15,30,60,90,120,150,180,210,240,270,300]
    colours = [["gold"]*3,["red"]*2,["deepskyblue"]*2,["black"]*2,["white"]*2]
    flattened_colours = [colour for sublists in colours for colour in sublists]
    return sizes, flattened_colours

# iterates through the size and colour lists to plot the circles for the target face
def plot_target_face_and_ref_line(ax,size_list,colour_list):
    ax.refline(x=0,y=0)
    for i in range(11):
        ax.ax_joint.plot([0],[0],'o',ms=size_list[i],mec=colour_list[i],mfc='none')
  
# procedure to set the x/y labels and limits
def set_params():
    plt.xlabel("Windage")
    plt.ylabel("Elevation")
    plt.axis([-1,1,-1,1])

# procedure which will save the plots to the previously chosen output
# file
def save_figure(output_dir,type): # <-- procedure for a single line lmao thats dumb
    plt.savefig(output_dir+"/"+type+".png",dpi=300)

# call the set_size_and_colour_list function and return size_list and colour_list
size_list, colour_list = set_size_and_colour_list()

# Plots ax1 --> KDE Plot
ax1 = sns.jointplot(data=df,x="x",y="neg_y",kind="kde",fill=True)
plt.title("KDE Plot (Kernel Distribution Estimate)", y=0)
set_params()
plot_target_face_and_ref_line(ax1,size_list,colour_list)
save_figure(output_dir,"kde-plot")

# Plots ax2 --> Scatter plot
ax2 = sns.jointplot(data=df,x="x",y="neg_y",marker="+",color="black")
plt.title("Scatter Plot w/ distributions", y=0)
set_params()
plot_target_face_and_ref_line(ax2,size_list,colour_list)
save_figure(output_dir,"scatter-plot")

# opens the output dir at end of runtime so the user has easy access to the previously plotted graphs
os.startfile(output_dir)
