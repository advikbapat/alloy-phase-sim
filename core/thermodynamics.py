import alloy_db

# for a binary solution compute the gibbs energy of each phase
# given 2 free energy curves, construct a common tangent to find the ends of the tie line
# get a phase diagram

"""
def get_free_energy_curves(system, T, composition_range):
    # Returns: dict of {phase_name: (x_array, G_array)}

def get_phase_boundaries(system, T):
    # Returns: list of (x_alpha, x_beta) tuples for each two-phase region

def get_phase_diagram(system, T_range, composition_range):
    # Returns: DataFrame with columns [T, phase, x_start, x_end]

def get_equilibrium_phases(system, T, x):
    # Returns: dict of {phase_name: phase_fraction} at a single (T, x) point
    # This is what Member B needs for nucleation driving force
"""

def get_phase_energy(metal, phase, T): 
    gibbs_base = 0
    phase_db = alloy_db.data[metal][phase]
    for g in phase_db["gibbs"]:
        if g["t_min"] <= T < g["t_max"]:
            gibbs_base = g["expression"](T)
            break
    
    # add gibbs magnetic and gibbs pressure

    return gibbs_base

