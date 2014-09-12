name = 'Zed A. Shaw'
age = 35.0
height = 74.0 #inches
weight = 180.0 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_to_centi = round(height * 2.54)
lbs_to_kg = round(weight * 0.453592)

print "Let's talk about %s." % name
print "He's %d centimeters tall." % in_to_centi
print "He's %d kilograms heavy." % lbs_to_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, in_to_centi, lbs_to_kg, age + in_to_centi + lbs_to_kg)
