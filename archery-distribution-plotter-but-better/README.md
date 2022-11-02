The old code felt clunky so I redid it all :)

CSV Data is from the MyTargets Archery app for Android

Changes
- Will now plot both a KDE Plot and a Scatter Plot (as opposed to only KDE Plot)
- Asks the user to select an output file and now saves the plots instead of only showing them previously
- --> The benefit of this is that the target face cirlces are now saved onto the image rather than just overlayed on top of the plot
- I tried to put anything that was used multiple times into functions; this improves readability and maintainability.

Deprecated from previous version
- Removed the suptitle
- Removed the suptitle dependencies
```
df["index"] = [i+1 for i in range(len(df))]

date = df["Date"]
round = df["Standard round"]
arrow = df["index"]

title = f"{round[0]} on {date[0]}: N={arrow[len(arrow)-1]}\n"

plt.title(title, y=-0.05)
```
