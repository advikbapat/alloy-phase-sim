# IRON - Fe
# a, b, c, d, e, f, g -> 0, 1, ln, 2, 3, -1, -9
import numpy as np

np.log(3)

data = {"Fe" :
        {
            "BCC_A2": 
                {
                    "magnetic":
                        {"Tc": 1043, "B0": 2.22},
                    "bulk":
                        {"A": 7.042095E-6, "a0": 2.3987E-5, "a1": 2.569E-8, "K0": 5.965E-12, "K1": 6.5152E-17, "n": 4.7041},
                    "gibbs":
                        [
                            {
                                "t_min": 298.15, 
                                "t_max": 1811, 
                                "expression": lambda T: 1225.7 + 124.134 * T - 23.5143 * T * np.log(T)  - 4.39752E-3 * np.pow(T, 2) - 0.058927E-6 * np.pow(T, 3) + 77359 / T 
                            },
                            {
                                "t_min": 1811, 
                                "t_max": 6000, 
                                "expression": lambda T: -25383.581 + 299.31255 * T -46 * T * np.log(T) + 2296.03E28 * np.pow(T, -9)
                            }
                        ]
                }
         }
        }