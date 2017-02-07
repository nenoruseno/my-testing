# Function for definition of departure procedures
# ================================================
def departure(file_name):
    import datetime
    file = open("neno.scn", "a")
    
# Read data from flight data file
    read2 = open("flights_data.txt", "r")
    data1 = read2.readlines()
    read2.close

    file.writelines(["# Departure procedures"])
    file.write("\n")

# Split flight data
    airc = data1[1].split()

    for j in range(len(airc)):
        aircraft = airc[j]

# Read data from departure procedures file
        read4 = open(file_name, "r")
        data3 = read4.readlines()
        read4.close

        m = len(data3)/3 # number of departure procedures

        for k in range(m):
            app_head = data3[3*k+0].split()
            app_wpt = data3[3*k+1].split()
            app_alt = data3[3*k+2].split()

# interval between created flights
            c = datetime.timedelta(seconds=j*k*int(data1[2]))  # interval in seconds (ex. 5 seconds)
            flight = data1[0].rstrip()+str(2)+str(k)+str(j)
            altitude = app_head[5]
            speed = app_head[4]
            orig = app_head[0]
            rwy_orig = app_head[1]
            dest = app_head[2]
            rwy_dest = app_head[3]
       
# Heading of departure procedure
            file.writelines([str(c), ">CRE ", flight, " ", aircraft, " ", orig, " ", rwy_orig, " * 0 0"])
            file.write("\n")
            file.writelines([str(c), ">ORIG ", flight, ", ", orig, ", ", rwy_orig])
            file.write("\n")
            file.writelines([str(c), ">DEST ", flight, ", ", dest, ", ", rwy_dest])
            file.write("\n")
            file.writelines([str(c), ">SPD ", flight, " ", speed])
            file.write("\n")
            file.writelines([str(c), ">ALT ", flight, " ", altitude])
            file.write("\n")
            
# Waypoint of departure procedure
            for l in range(len(app_wpt)):
                wpt_name = app_wpt[l]
                wpt_alt = app_alt[l]
            
# writing to scenario file
                file.writelines([str(c), ">ADDWPT ", flight, ", ", wpt_name, ", ", wpt_alt])
                file.write("\n")

    file.close()

    return
