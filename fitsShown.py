from astropy.io import fits
import matplotlib.pyplot as plt

hdul = fits.open('simulated_image.fits')
data = hdul[0].data  # en imágenes, la data siempre está en la extensión 0

plt.imshow(data, origin='lower', cmap='gray')
plt.colorbar(label='Intensidad')
plt.title('Imagen FITS simulada')
plt.show()
