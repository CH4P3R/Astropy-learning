from astropy import units as u

distanceToSun = 1 * u.AU
print("Distance to sun in KM:" ,distanceToSun.to(u.km))
print("Distance to sun in AU:" ,distanceToSun)