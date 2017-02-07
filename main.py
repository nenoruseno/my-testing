# Python Script for Creating Scenario File
# in BlueSky ATM Simulation
# Created by Neno Ruseno
# Version 1.2
# ========================================

print "Creating Scenario file for BluSky ATM Simulation....."

# Definition of unpublished waypoints
from waypoint import waypoint
waypoint("unpublished_waypoints.txt")

# Definition of arrival procedures
from arrival import arrival
arrival("arrival_procedures.txt")

# Definition of departure procedures
from departure import departure
departure("departure_procedures.txt")

print "The scenario file is created as neno.scn, please check it!"

# END
