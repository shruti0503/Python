#dividing a single array into multiple smaller array
#splitfunction -> array, no of axis / arr of sp , axis 

#axis paramters:  axis=0 -> vertically , axis=1 -> 
#Number of splits
#SplitPoints
#Vertical/Horizontal Scaling
#hSplit/Vsplit
#Broadcasting
#Performace considertions

# np.split(array,3)
# np.vsplit(array,2)
# np.nsplit(array,2)


##################

# Vertical and Horizontal Splitting:

# Vertical splitting divides the array into smaller arrays along its rows,
# creating sub-arrays with the same number of columns.
# Horizontal splitting divides the array into smaller arrays along its columns,
# creating sub-arrays with the same number of rows.

# hsplit and vsplit:

# NumPy provides convenience functions numpy.hsplit 
#   and numpy.vsplit for splitting arrays horizontally and vertically, respectively.
  
# These functions are equivalent to using split with axis=1 
#   for hsplit and axis=0 for vsplit.

