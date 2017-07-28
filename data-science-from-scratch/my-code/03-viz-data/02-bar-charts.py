#  ** Bar Charts
from matplotlib import pyplot as plt
from collections import Counter

#   - Good for showing how some quantity varies amongst some discrete set
#   of items
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bars are by default width 0.8, so we'll add 0.1 to the left coords
# to ensure that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x coords [xs], heights [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()

#   - Bar charts are also useful for histograms with bucketed numeric values
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],
        histogram.values(),
        8)

plt.axis([-5, 105, 0, 5])  # x axis and y axis

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

#   - It is considered bad practice for your y-axis not to start at 0 ??
mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science'")

# If you don't do this, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner
plt.ticklabel_format(useOffset=False)

# misleading y-axis only shows the part above 500
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' Increase!")
plt.show()  # TODO: figure out why the bar's aren't centered

# more sensible axis
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Not so Huge Anymore")
plt.show()
