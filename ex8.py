formatter = "%r %r %r %r" #creates the variable formatter

print formatter % (1, 2, 3, 4)  #replaces every '%r' in formatter with its assigned digit
print formatter % ("one", "two", "three", "four")   #replaces every '%r' in formatter with its assigned string
print formatter % (True, False, False, True)    #replaces every '%r' in formatter with its assigned boolean
print formatter % (formatter, formatter, formatter, formatter)  #replaces every '%r' in formatter with the variable formatter
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
