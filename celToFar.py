"""
	Functions for temperature conversions
	from farenheight to celcius
	and vice versa.
"""
def convert(cel):

    if cel <= -273.15:
        return "that temperature cannot exist"
    else:
        far = cel* 9/5 + 32
    return far

def calCLen (string):
    if type(string) == 'str':
        length = len(string)
        return length
    else:
        print("other types do not have length")

temperatures=[10,-20,-289,100]
def create():

    with open("temperature",'w+') as file:

        for temp in temperatures:
            convert(temp)
            file.write(str(temp) + '\n')
