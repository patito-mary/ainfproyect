import numpy as np
import pandas as pd

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
            self.cols      = list(np.arange(0,24)) #all

        self.path = path; self.file = file; self.read()
        
    def read(self):
        """function to read the data to show like table using .data
        """
        if self.file == "*.hdf5":
            print("No se ha hecho esta parte")
        else:
            table = np.genfromtxt(str(self.path+self.file), usecols = self.cols, names=True)
            # Here i change the np for pandas, to make easy the functions to the data
            self.data = table
        return(self.data)


    def halo_info(self, index, info=False): 
        """function to access to the index of the row with data. 

        Args:
            index (_type_): index from the row with data
            info (bool, optional): return (or not) the data of the row
        """
        self.hinfo = self.data[index]
        return(self.hinfo)

#cinematica entre DOS halos
class kinetic:                                   
    
    def __init__(self, halo1, halo2):          #halo1 y halo22 son objetos de read_file (halo_info)  
        self.halo1 = halo1; self.halo2 = halo2     

    def distance(self): 
        posA = self.halo1[4:]; posB = self.halo2[4:]
        distance = np.linalg.norm(posA-posB)
        return(distance)
    
    #def velocity(self, , halo2): 
        #return(np.linalg.norm(halo1-halo2))
    



