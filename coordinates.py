from astropy.coordinates import SkyCoord
import astropy.units as u

c = SkyCoord(ra=10.684*u.degree, dec=41.269*u.degree, frame="icrs")

gal = c.transform_to("galactic")

print(c)    
print(gal)  