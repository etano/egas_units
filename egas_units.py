import sys, os
from math import pow, sqrt, pi

class Units:
    def __init__(self, energy_units_type, length_units_type):

        self.energy_units_type = energy_units_type
        if self.energy_units_type == 0:
            print '*** Using Hartree ***'
        elif self.energy_units_type == 1:
            print '*** Using Rydberg ***'
        elif self.energy_units_type == 2:
            print '*** Using Kelvin ***'
        else:
            print 'ERROR: Unrecognized energy units type!'
            sys.exit()

        self.length_units_type = length_units_type
        if self.length_units_type == 0:
            print '*** Using Bohr radii ***'
        elif self.length_units_type == 1:
            print '*** Using Wigner-Seitz radii ***'
        elif self.length_units_type == 2:
            print '*** Using Angstroms ***'
        else:
            print 'ERROR: Unrecognized length units type!'
            sys.exit()

    def ConvertEnergy(self,E):
        """ Input is energy in atomic units """
        if self.energy_units_type == 0:
            return E
        elif self.energy_units_type == 1:
            return 2.*E
        elif self.energy_units_type == 2:
            return 315775.13*E # Source: 2014 CODATA

    def ConvertLength(self,rs,L):
        """ Input is length in atomic units """
        if self.length_units_type == 0:
            return L
        elif self.length_units_type == 1:
            return L/rs
        elif self.length_units_type == 2:
            return L/0.52917721067 # Source: 2014 CODATA

    def GetTF(self,rs,D,pol):
        """ Fermi temperature """
        if D == 3:
            TF = 0.5*(9.*pi/4.)**(2./3.) / (rs**2)
        elif D == 2:
            TF = 1./(rs**2)
        else:
            print "ERROR: D must equal 2 or 3!"
            sys.exit()
        if pol:
            TF = TF * pow(2.,2./D)
        return self.ConvertEnergy(TF)

    def GetT(self,rs,D,pol,theta):
        """ Temperature """
        return theta*self.GetTF(rs,D,pol)

    def GetL(self,rs,D,N):
        """ Length of box """
        if D == 3:
            L = rs * pow(4.*N*pi/3., 1.0/3.0)
        elif D == 2:
            L = rs * sqrt(pi*N)
        else:
            print "ERROR: D must equal 2 or 3!"
            sys.exit()
        return self.ConvertLength(rs,L)

    def GetLam(self,rs):
        """ \hbar^2/2m (has units of energy * distance^2) """
        return self.ConvertLength(rs,self.ConvertLength(rs,self.ConvertEnergy(0.5)))

    def GetEps(self,rs):
        """ \epsilon  = Z1*Z2 (has units of energy * distance) """
        return self.ConvertLength(rs,self.ConvertEnergy(1.))

def usage():
    print "Usage: %s rs D pol theta N (energy_units_type) (length_units_type)" % os.path.basename(sys.argv[0])
    sys.exit(2)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if "-h" in argv or "--help" in argv:
        usage()

    try:
        rs = float(sys.argv[1])
        D = int(sys.argv[2])
        pol = int(sys.argv[3])
        theta = float(sys.argv[4])
        N = int(sys.argv[5])
    except:
        usage()

    try:
        energy_units_type = int(sys.argv[6])
        length_units_type = int(sys.argv[7])
    except:
        energy_units_type = 0
        length_units_type = 0

    e = Units(energy_units_type,length_units_type)
    print "T_F", e.GetTF(rs,D,pol)
    print "T", e.GetT(rs,D,pol,theta)
    print "L", e.GetL(rs,D,N)
    print "\hbar^2/2m", e.GetLam(rs)
    print "Z1*Z2", e.GetEps(rs)

if __name__ == "__main__":
    sys.exit(main())
