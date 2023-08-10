#Primary Fur Color
#How many Gray, Cinnamon and Black squirrels

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

nr_of_grey = len(data[data["Primary Fur Color"] == "Gray"])
nr_of_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
nr_of_black = len(data[data["Primary Fur Color"] == "Black"])

# Create list for color and number of squirrels
colors = ["Gray", "Cinnamon", "Black"]
nr_of_squirrels = [nr_of_grey, nr_of_cinnamon, nr_of_black]

# Create a dictionary with the colors and the counts
count_by_color_dict = {
    "color": colors,
    "count": nr_of_squirrels
}
data = pandas.DataFrame(count_by_color_dict)
data.to_csv("squirrels count.csv")
print(data)

