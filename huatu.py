# from uwb_radar import uwb_radar
# import tools
# from time import sleep
#
import numpy as np
#
# import os
import matplotlib.pyplot as plt
# import matplotlib as mp

signal=[9.20793936e-09,1.74747222e-09,3.83495212e-09,3.40658679e-09,1.46414776e-09,3.51262489e-09,8.33118901e-10,3.27925564e-09]

plt.figure()
plt.plot(np.arange(len(signal)), signal, label='Smooth', color='r', marker="*")
plt.xlabel(xlabel='y (Å)')
plt.ylabel(ylabel='Number ratio')
plt.legend()
#plt.xlim((0, 5))
plt.show()