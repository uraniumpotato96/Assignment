"""
	Basic program for conversion of minutes to seconds.

"""
def convert():
    min = float(input('enter the minutes to be converted '))
    hours = min/60.0
    return hours
print(convert())
