# creation for python class
python_class={'Mark', 'Megan', 'Dave'}
print(python_class)

# creation for web class
web_class={'Joe', 'Mike', 'Dave'}
print(web_class)

# this is finding people who are in both classes
same = python_class|web_class

# this is finding the people who are just in one class
different = python_class^web_class

print("list of students who are attending both the classes: %s"%(same))
print("list of students who are not common in both the classes: %s"%(different))