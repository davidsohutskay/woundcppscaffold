"""
Generates design points on which you should evaluate the model.

Feel free to change stuff accordingly.

This requires installing pyDOE which you can do by:

    pip install pyDOE


The design we are going to use is called a Latin Hypercube Design.

"""

import pyDOE as pd
import numpy as np

# Specify how many simulations you can afford:
num_simulations = 200

# Constants

# Specify the lower and upper bounds of your model inputs
# I am not using exactly your numbers. I am rounding up or down.
# The purpose here is to cover the range of possible inputs as well
# as possible.
# [left, right] bounds
bounds = np.array([[0.0511/10, 0.0511*100], # k_0 [MPa]
                   [0.015/10, 0.015*100], # kf [MPa]
                   [0.048/10, 0.048*100], # k2 [-]
                   [0,np.pi], # mu
                   [0.0, 0.5], # kappa
                   [0.01, 1.0], # phif_scaffold [-]
                   [0.000970, 0.000970*100], # d_phif_scaffold [/hr]
                   [0.0, 0.1]]) # d_c_phif_rho [g/mm3]

# Other interesting parameters
# t_rho, K_t, tau_lamdaP, D_0/D_inf, H

# The number of inputs that you have:
num_inputs = bounds.shape[0]

# Now I sample designs in [0,1]^3 and I am going to scale them back to the
# original bounds
X_scaled = pd.lhs(num_inputs, num_simulations)

# Let's get to the original space
X = X_scaled * (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]

# Split into a few separate runs
X1 = X[0:200,:]
# X2 = X[400:800,:]
# X3 = X[800:1200,:]

# Save to a text file
np.savetxt('samples_to_run.txt', X1, fmt='%.6f')
# np.savetxt('samples_to_run_2.txt', X2, fmt='%.6f')
# np.savetxt('samples_to_run_3.txt', X3, fmt='%.6f')

# You must do all these simulations...
