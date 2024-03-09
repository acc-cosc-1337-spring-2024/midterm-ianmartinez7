#add import

# This is the global variable that will be modified by use_global function.
from question_b import  use_global


print("Before calling: ", use_global)
use_global = "Changed value"
print("After calling: ", use_global)


