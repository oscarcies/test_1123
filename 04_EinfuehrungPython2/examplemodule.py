# Import other necessary modules
import math


# Definition of module-related variables
# Euclidean coordinated in three dimensions, examples
coord1 = [1, 5, 7]
coord2 = [3, 3, 8]
coord3 = [8, 4, 3]
coord4 = [7, 5, 7]

# Function to calculate euclidean distance metric
def calcEuclideanDist(c1, c2):
    """
    The examplemodule, imported below, contains some example coordinates in 3-dimensional space.
    Furthermore it defines a function to calculate the euclidean distance between two points in 3-dimensional space, according to

    𝑑(𝑥,𝑦)=(𝑥1−𝑦1)^2+(𝑥2−𝑦2)^2+(𝑥3−𝑦3)^2
    """
    return math.sqrt(pow(c1[0]-c2[0], 2) + pow(c1[1]-c2[1], 2) + pow(c1[2]-c2[2], 2))
