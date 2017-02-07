# Function for definition of unpublished waypoints
# ================================================
def waypoint(file_name):

    file = open("neno.scn", "w")
    file.writelines(["# Scenario file for BlueSky ATM simulation"])
    file.write("\n")
    file.writelines(["# ----------------------------------------"])
    file.write("\n")

# Read data from unpublished waypoints file
    read1 = open(file_name, "r")

# writing to scenario file
    file.writelines(["# Definition of unpublished waypoints"])
    file.write("\n")

    for line in read1:
        file.writelines(["0:00:00.00>DEFWPT ", line])

    file.write("\n")

    file.close()

    return
