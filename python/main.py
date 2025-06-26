import numpy as np
import matplotlib.pyplot as plt

def calculate_epsilon_eff(er, w_h):
    """Calculates effective permittivity."""
    return (er + 1) / 2 + (er - 1) / (2 * np.sqrt(1 + 12 / w_h))

def calculate_Z0(er, w_h):
    """Calculates characteristic impedance."""
    epsilon_eff = calculate_epsilon_eff(er, w_h)
    
    if w_h <= 1:
        Z0 = (60 / np.sqrt(epsilon_eff)) * np.log(8 / w_h + w_h / 4)
    else:
        Z0 = (120 * np.pi / np.sqrt(epsilon_eff)) / (w_h + 1.393 + 0.667 * np.log(w_h + 1.444))
    return Z0

# Define parameters
er_values = [2, 4, 6, 8, 10]
w_h_values = np.linspace(0.1, 10, 500) # Range of W/h values

plt.figure(figsize=(10, 6))

for er in er_values:
    Z0_values = [calculate_Z0(er, wh) for wh in w_h_values]
    plt.plot(w_h_values, Z0_values, label=f'$\epsilon_r = {er}$')

plt.title('$Z_0$ versus $w/h$ for different $\epsilon_r$ values')
plt.xlabel('$w/h$ ratio')
plt.ylabel('$Z_0$ ($\Omega$)')
plt.grid(True)
plt.legend()
plt.ylim(0, 150) # Set a reasonable y-limit for better visualization
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8 # Speed of light in vacuum
mu0 = 4 * np.pi * 1e-7 # Permeability of free space
sigma_copper = 5.8e7 # Conductivity of copper 
h_substrate = 1.27e-3 # Substrate thickness in meters
t_conductor = 8.89e-6 # Conductor thickness in meters
er_substrate = 10.8 # Relative permittivity of substrate 
tan_theta = 0.0028 # Loss tangent of substrate 
Z0_target = 50 # Target characteristic impedance 

# Calculated w/h and epsilon_eff from part (a)
w_h_calculated = 0.886
epsilon_eff_calculated = 7.1848
W_calculated = w_h_calculated * h_substrate

def calculate_skin_depth(f, sigma, mu):
    return 1 / np.sqrt(np.pi * f * mu * sigma)

def calculate_Rs_thin(f, sigma, mu, t):
    delta = calculate_skin_depth(f, sigma, mu)
    return 1 / (sigma * delta * (1 - np.exp(-t / delta)))

def calculate_alpha_c(f, Z0, w, sigma_c, mu_c, t_c):
    Rs = calculate_Rs_thin(f, sigma_c, mu_c, t_c)
    return 8.686 * Rs / (w * Z0) # dB/m 

def calculate_alpha_d(f, er, eff_er, tan_delta, u_prop):
    lambda_g = u_prop / f # Wavelength in the line 
    return 27.3 * ((eff_er - 1) * er) / ((er - 1) * eff_er) * tan_delta / lambda_g # dB/m 

# Frequency range from 1 GHz to 20 GHz
frequencies_GHz = np.linspace(1, 20, 100)
frequencies_Hz = frequencies_GHz * 1e9

alpha_c_values = []
alpha_d_values = []
alpha_total_values = []

# Calculate phase velocity (constant with frequency in TEM approximation)
u_propagation = c / np.sqrt(epsilon_eff_calculated)

for freq in frequencies_Hz:
    alpha_c_val = calculate_alpha_c(freq, Z0_target, W_calculated, sigma_copper, mu0, t_conductor)
    alpha_d_val = calculate_alpha_d(freq, er_substrate, epsilon_eff_calculated, tan_theta, u_propagation)
    
    alpha_c_values.append(alpha_c_val)
    alpha_d_values.append(alpha_d_val)
    alpha_total_values.append(alpha_c_val + alpha_d_val)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies_GHz, alpha_c_values, label='Attenuation in conductor ($\\alpha_c$)')
plt.plot(frequencies_GHz, alpha_d_values, label='Attenuation in dielectric ($\\alpha_d$)')
plt.plot(frequencies_GHz, alpha_total_values, label='Total attenuation ($\\alpha_{total}$)', linestyle='--')

plt.title('Attenuation vs. Frequency for $Z_0 = 50\Omega$ Microstrip Line')
plt.xlabel('Frequency (GHz)')
plt.ylabel('Attenuation (dB/m)')
plt.grid(True)
plt.legend()
plt.show()