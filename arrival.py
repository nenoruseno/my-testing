# Function for definition of arrival procedures
# ================================================
def arrival(file_name):
    import datetime
    file = open("neno.scn", "a")
    
# Read data from flight data file
    read2 = open("flights_data.txt", "r")
    data1 = read2.readlines()
    read2.close

    file.writelines(["# Arrival procedures"])
    file.write("\n")

# Split flight data
    airc = data1[1].split()

    for j in range(len(airc)):
        aircraft = airc[j]
        
# Read data from approach procedures file
        read3 = open(file_name, "r")
        data2 = read3.readlines()
        read3.close

        n = len(data2)/3 # number of approach procedures

        for k in range(n):
            app_head = data2[3*k+0].split()
            app_wpt = data2[3*k+1].split()
            app_alt = data2[3*k+2].split()

# interval between created flights
            c = datetime.timedelta(seconds=k*j*int(data1[2]))  # interval in seconds (ex. 5 seconds)
            flight = data1[0].rstrip()+str(1)+str(k)+str(j)
            coordinate = app_wpt[0]
            heading = app_head[4]
            altitude = app_alt[0]
            speed = app_head[5]
            orig = app_head[0]
            rwy_orig = app_head[1]
            dest = app_head[2]
            rwy_dest = app_head[3]
       
# Heading of approach procedure
            file.writelines([str(c), ">CRE ", flight, ", ", aircraft, ", ", coordinate, ", ", heading, ", ", altitude, ", ", speed])
            file.write("\n")
            file.writelines([str(c), ">ORIG ", flight, ", ", orig, ", ", rwy_orig])
            file.write("\n")
            file.writelines([str(c), ">DEST ", flight, ", ", dest, ", ", rwy_dest])
            file.write("\n")
            
# Waypoint of approach procedure
            for l in range(len(app_wpt)-2):
                wpt_name = app_wpt[l]
                wpt_alt = app_alt[l]
            
# writing to scenario file
                file.writelines([str(c), ">ADDWPT ", flight, ", ", wpt_name, ", ", wpt_alt])
                file.write("\n")

            file.writelines([str(c), ">ADDWPT ", flight, ", ", app_wpt[len(app_wpt)-2], " ", app_wpt[len(app_wpt)-1], ", ", app_alt[len(app_alt)-1]])
            file.write("\n")

    file.close()

    return
