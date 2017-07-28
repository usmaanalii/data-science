# * Basics

# ** Whitespace Formatting
#   - Whitepace is ignored inside parenthesis and brackets, helping with
#   readability and Formatting
#   - You cna also use + \

# ** Modules
#   - import re as regex is referred to as 'using an alias'

# ** Functions
#   - A function is a rule for taking zero or more inputs and returning a
#   corresponding output
#   - Don't assign lambdas to variables!

# ** Strings
#   - Use raw strings r"" if you want to use \ in the string without escaping

# ** Lists
#   - Python has an in operator to check if an element is a member of a Lists
#   e.g 1 in [1, 2, 3]

# ** Tuple
#   - You can specify a tuple without parenthesis e.g tuple = 1, 2
#   - Useful for returning multiple values from functions
#   e.g return x, y

# ** Dictionary
#   - You can check for the existence of a key, like lists e.g "x" in dict
#   - You can use the get method, and provide a fedault value, avoiding the
#   raising of an exception
#   e.g dict.get("key", 0)
#   - Dictionary keys must be immutable, so you can't use a list as a key

# ** defaultdict
#   - Like a regular dictionary, but adds a value when the key doesn't exist,
#   you provide this value
#   e.g defaultdict(list) or defaultdict(int)

# ** Counter
#   - This will turn sequences of values into defaultdict's with a default
#   value of int, its useful for histograms

# ** Control Flow
#   - Python returns the second value for an 'and' statement if the first
#   is true
#   - It will also return the first statement in an 'or' if the second
#   is false
#   - So you can use assignments like so...
#   e.g var_1 = s and s[0]  this will set var_1 = s[0] if s is truthy
#       var_2 = x or 0  this will set var_2 = x
