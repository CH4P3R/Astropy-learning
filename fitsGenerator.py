from astropy.io import fits
import numpy as np

# Crear una imagen de 100x100 pixeles
data = np.random.random((100, 100))  # valores aleatorios entre 0 y 1

# Crear un header opcional
header = fits.Header()
header['OBJECT'] = 'Simulated'
header['TELESCOP'] = 'PythonScope'
header['FILTER'] = 'V'

# Crear el HDU principal con los datos y header
hdu = fits.PrimaryHDU(data=data, header=header)

# Crear el archivo FITS
hdu.writeto('simulated_image.fits', overwrite=True)

print("Archivo FITS creado: simulated_image.fits")
