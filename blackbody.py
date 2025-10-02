#Plot the Planck law curve for a blackbody.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson


T_list = [4000,5000,6000]
star_temps = {
    'Sun': 5778,
    'Sirius': 9940,
    'Betelgeuse': 3500
}
# print("Temperature inputs are: ", T_list)

wavelengths = np.linspace(100e-9, 3000e-9, 500)  # Wavelengths from 100 nm to 3 µm
h = 6.626e-34  # Planck's constant (J·s)
c = 3.0e8      # Speed of light (m/s)
k = 1.381e-23  # Boltzmann's constant (J/K)

def planck_law(wavelength, T):
    exponent = (h * c) / (wavelength * k * T)
    radiance = (2 * h * c**2) / (wavelength**5 * (np.exp(exponent) - 1))
    return radiance

plt.figure(figsize=(8,5))

for star, T in star_temps.items():
    radiance = planck_law(wavelengths, T)
    peak_index = np.argmax(radiance)
    peak_wavelength = wavelengths[peak_index]
    print(f"Peak wavelength for T = {T} K is: {peak_wavelength * 1e9:.2f} nm")

    total_radiance = simpson(radiance, wavelengths)
    flux = np.pi * total_radiance    
    print(f"Total radiated power per unit area for T = {T} K is: {total_radiance:.2e} W/m^2")
    
    plt.plot(wavelengths * 1e9, radiance, label=f'{star}: {T} K')

plt.axvspan(380, 750, color='grey', alpha=0.2, label='Visible Light')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Spectral Radiance')
plt.title('Planck Law curve comparison at different temperatures')
plt.grid(True)
plt.legend()
plt.show()