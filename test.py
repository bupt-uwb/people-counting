import numpy as np
import json
# listR = [0,1,0,1,0,1,1,0,1,0,1,1]
renshu = 0
radar = 1
# try:
#     with open('data.txt', 'w') as listfile:
#         # listfile.write('\n')
#         listR.append(renshu)
#         listR.append(radar)
#         # listR.append('\r\n')
#         listfile.write(str(listR))
#         listfile.write('\n')
#         listfile.close()
# except:
#     print('load wrong')


data = np.loadtxt('Test.txt', dtype=np.int, delimiter=',')
print(data)