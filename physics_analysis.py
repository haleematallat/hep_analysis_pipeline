import numpy as np

def calculate_invariant_mass(px1, py1, pz1, E1, px2, py2, pz2, E2):
    """
    Calculate the invariant mass of two particles using their momentum and energy.
    """
    # Energy-momentum components for each particle
    E_total = E1 + E2
    px_total = px1 + px2
    py_total = py1 + py2
    pz_total = pz1 + pz2
    
    # Invariant mass formula
    invariant_mass = np.sqrt(E_total**2 - (px_total**2 + py_total**2 + pz_total**2))
    return invariant_mass
