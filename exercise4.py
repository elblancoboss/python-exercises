"""4. Functions
•	Explore the function frequency and its parameters.
•	Using the function frequency, write a function that will produce a histogram from
a list. A histogram shows in a visual fashion, such as with stars, the number of times an item occurs in a list. For example, the histogram for the data used to illustrate the frequency function might appear as follows:

abc ***
pdq *
def *

•	What type of value is returned by has_key()? Explain why you can nevertheless use this value in a Boolean test, such as an if statement or a while.
"""

#4. Functions
from collections import Counter
list1 = ['abcd', 'abcd', 'abcd', 278, '18 Feb 2016']
counts = Counter(list1)
print(counts)
print("\n")

#has_key() was removed in Python 3.x. use the in operator instead.
#has_key() provides boolean value, its either "true" or "false".
