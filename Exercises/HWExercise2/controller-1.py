import math
import numpy as np
import rospy

class Controller():

    def __init__(self):
        self.v_ref = 0.22
	self.rho_ref = 0.1

    def getControlOutput(self, rho, theta, psi, t_delay, dt_last):
        #TODO: Implement your own follow-the-leader controller
	v_out = 
        omega_out = 
                       
        return (v_out, omega_out)
