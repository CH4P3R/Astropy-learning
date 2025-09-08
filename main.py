from astropy import units as u
from astropy.constants import c

distancia = 4.2 * u.lightyear
tiempo = 2 * u.year

vel = distancia / tiempo
print(vel.to(u.km/u.s)) 

print(c.to(u.km/u.s))
