import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.mean(speed)
print(x)

x = numpy.median(speed)
print(x)

x = stats.mode(speed)
print(x)

# Standard deviation is a number that describes how spread out the values are
x = numpy.std(speed)
print(x)

# Variance is another number that indicates how the values are spread out
# multiply the standard deviation by itself to get the variance
x = numpy.var(speed)
print(x)

# the formula to find the standard deviation is the square root of the variance
# Standard Deviation is often represented by the symbol Sigma: σ
# Variance is often represented by the symbol Sigma Squared: σ2
x = numpy.std(speed)
print(x)

# Percentiles are used to return a number that describes the values that are lower than a given percent of values
x = numpy.percentile(ages, 75)
print(x)

# What age of the people are younger than 90%?
x = numpy.percentile(ages, 90)
print(x)

x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

plt.hist(x, 10)
plt.show()

# use the array from the numpy.random.normal() method, with 100000 values
# to draw a histogram with 100 bars.
# specify that the mean value is 5.0, and the standard deviation is 1.0.
# Meaning the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
# most values are between 4.0 and 6.0, with a top at approximately 5.0.
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()

# create an array where the values are concentrated on a given value
x = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(x, 1000)
plt.show()

# Reverse the entire data structure
var = x[::-1]
print(x)

