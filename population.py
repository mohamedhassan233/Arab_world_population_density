#The collection of Arab countries in the world
countries={1:'Egypt',2:'Algeria',3:'Sudan',
           4:'Iraq',5:'Morocco',6:'Saudi Arabia',7:'Yemen',8:'Syria',9:'Tunisia',
           10:'Jordan',11:'United Arab Emirates',12:'Libya'
    ,13:'Lebanon',14:'Palestine',15:'Oman',16:'Kuwait',17:'Qatar',18:'Bahrain'}

#This program reads data files of country populations and areas and prints the
# population density for each country.
POPULATION_FILE = "pop.txt"
AREA_FILE = "area.txt"
POPULATION_DENSITY_REPORT = "density_report.txt"

def main() :
    # Open the files.
    popFile = open(POPULATION_FILE, "r")
    areaFile = open(AREA_FILE, "r")
    reportFile = open(POPULATION_DENSITY_REPORT, "w")

    density = 0.0
    id=1

    popRead=popFile.readline()
    areaRead=areaFile.readline()
    while popRead != '' :
        population=float(popRead)
        area=float(areaRead)
        if area==0:
            break         # Protect against division by zero.
        density=population/area
        reportFile.write('%s population density is:  %.2f\n'%(countries[id],density))
        id+=1
        popRead=popFile.readline()

    # Close the files.
    popFile.close()
    areaFile.close()
    reportFile.close()

# Start the program.
main()