import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, colors, ticker, cm

#leer archivo:
class read_file: 
    """Class to charge things and access to the propiertes via object type
    """
    
    def __init__(self, path, file, columns=None):
        """_summary_

        Args:
            path (_type_): path to the folder of data
            file (_type_): name of the file with the data
            columns (_type_, optional): columns that you want to charge. Defaults to None.
        """
        if columns is not None:
            self.cols = columns
        else:
            #self.cols     = [0, 1, 2, 3, 5, 6, 7]        #ID, hosthalo, substruc, masa y posiciones xyz
            self.cols      = [1, 2, 3]                    #solo N. de sub y masa para el plot 2D.
        self.path = path; self.file = file; self.read()
        
    def read(self):
        if self.file == "*.hdf5":
            print("No se ha hecho esta parte")
        else:
            self.data = np.genfromtxt(str(self.path+self.file), usecols = self.cols, unpack=True)#, names=True)   
            #self.data = np.array([list(row) for row in data])#para poder hacer slicing


    def halo_info(self, index, info=False): 
        self.hinfo = self.data[index]
        return(self.hinfo)

#cinematica entre DOS halos
class kinetic:                                   
    
    def __init__(self, halo1, halo2):          #halo1 y halo22 son objetos de read_file (halo_info)  
        self.halo1 = halo1; self.halo2 = halo2     

    def distance(self): 
        posA = self.halo1[4:]; posB = self.halo2[4:]
        return(np.linalg.norm(posA-posB))
    
    #def velocity(self, , halo2): 
        #return(np.linalg.norm(halo1-halo2))
    



