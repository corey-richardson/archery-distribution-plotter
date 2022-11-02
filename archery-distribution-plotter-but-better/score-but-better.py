import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tkinter import filedialog as fd

# set input csv file and output directory using tkinters filedialog
input_file = fd.askopenfilename(filetypes=[("CSV files", "*.csv")],title="Set input .csv file")
output_dir = fd.askdirectory(title="Set output folder (plots will be saved here)")

# pandas read the csv and sanitise it for use
# the sign for "y" is flipped as the input data is w r o n g
df = pd.read_csv(input_file,sep=";")
df.replace("\"","")
df["neg_y"] = df["y"] * -1

sns.set_theme(style="darkgrid", palette="pastel")

# procedure which will plot the target face and reference line onto the 
# passed in graph
def plot_target_face_and_ref_line(ax):
    ax.refline(x=0, y=0)
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

# procedure to set the x/y labels and limits
def set_params():
    plt.xlabel("Windage")
    plt.ylabel("Elevation")
    plt.axis([-1,1,-1,1])

# procedure which will save the plots to the previously chosen output
# file
def save_figure(output_dir,type): # <-- procedure for a single line lmao thats dumb
    plt.savefig(output_dir+"/"+type+".png", dpi=300)

# Plots ax1 --> KDE Plot
ax1 = sns.jointplot(data=df,x="x",y="neg_y",kind="kde",fill=True)
plt.title("KDE Plot (Kernel Distribution Estimate)", y=0)
set_params()
plot_target_face_and_ref_line(ax1)
save_figure(output_dir,"kde-plot")

# Plots ax2 --> Scatter plot
ax2 = sns.jointplot(data=df,x="x",y="neg_y")
plt.title("Scatter Plot w/ distributions", y=0)
set_params()
plot_target_face_and_ref_line(ax2)
save_figure(output_dir,"scatter-plot")

