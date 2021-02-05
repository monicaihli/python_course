import numpy
from matplotlib import pyplot

# array from list using the .array() function
my_list = [3,5,6,9,5,6,5]
print(type(my_list))
a1 = numpy.array(my_list)
print(type(a1))
print("An array of dimensions: {}".format(a1.ndim))


# array from list of lists
my_lists = [[1,2,3,4,5,6,7],
            [3, 5, 6, 9, 5, 6, 5]]
print(type(my_lists))
a2 = numpy.array(my_lists)
print(type(a2))
print("An array of dimensions: {}".format(a2.ndim))

# plot some data from a numpy array
pyplot.title("Hi Laura")
pyplot.xlabel("Days")
pyplot.ylabel("Count")
pyplot.plot(my_list)
pyplot.savefig(fname='helloworld.png',format='png') # save the plot to an image file
pyplot.show() # display the plot
