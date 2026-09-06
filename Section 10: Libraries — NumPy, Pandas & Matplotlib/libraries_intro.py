#A library is a collection of
# pre-written code that someone else
# has already written for you!

# Think of it like a toolbox —
# instead of building every tool yourself —
# you just open the toolbox and use
# the tools that are already there!


import numpy
import pandas
import matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
from pandas import DataFrame

print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("matplotlib version:", matplotlib.__version__)

#Numpy-Math operations
#numbers=np.array[10,20,30,40,50]

# #Regular Python list:
# my_list = [10, 20, 30, 40, 50]
# print(my_list * 2)  # repeats the list!
# # Output: [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

#NumPy array:
# my_array = np.array([10, 20, 30, 40, 50])
# print(my_array * 2)  # multiplies EVERY item!
# # Output: [20, 40, 60, 80, 100]
# print("Mean:",np.mean(my_array))
# # print("Sum:",np.sum(my_array))

# data={
#     "Name":["Rahul","Priya","Amit"],
#     "Course":["BCA","B.E","BSC"],
#     "Marks":[85,92,78]
# }

# df=pd.DataFrame(data)
# print("\nStudent Data")
# print(df)


plt.plot([1,2,3,4,5],[10,20,30,15,25])
plt.title("Simple Line chart")
plt.xlabel("Xaxis")
plt.ylabel("Yaxis")
plt.show()