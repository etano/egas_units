# egas_units

Usage:

    python egas_units.py rs D pol theta N (energy_units_type) (length_units_type)
    
where

    rs = Wigner-Seitz radius
    D = # of physical dimensions (assuming box of equal side lengths)
    pol = polarization (0: unpolarized, 1: polarized)
    theta = ratio of temperature to Fermi temperature (T/T_F)
    (optional) energy_units_type = units for energies (0: Hartree (default), 1: Rydberg, 2: Kelvin)
    (optional) length_units_type = units for lengths (0: Bohr radii (default), 1: Wigner-Seitz radii, 2: Angstroms)
