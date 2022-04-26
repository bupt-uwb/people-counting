import numpy as np
from uwb_radar import uwb_radar
import tools
from time import sleep

import json

import os
import matplotlib.pyplot as plt
# import matplotlib as mp

'''
删除log文件
将json文件里的人数初始值置为0
'''
list_men=[]
def start():
    for files in os.listdir('.'):
        if files.endswith(".log"):
            os.remove(os.path.join('.', files))
    persons = {"1": 0}
    filename = 'Result.json'
    with open(filename, 'w') as file_obj:
        json.dump(persons, file_obj)
    file_obj.close()

'''
保存当前人数到json文件
'''
def save_json(filename, person):
    persons = {"1": person}
    with open(filename, 'w') as file_obj:
        json.dump(persons, file_obj)
    file_obj.close()


if __name__ == '__main__':
    start()
    args = {
        'set_enable':1,
        'set_iterations':64,
        'set_pulses_per_step':5,
        'set_dac_step':1,
        'set_dac_min':949,
        'set_dac_max':1100,
        'set_tx_power':2,
        'set_downconversion':0,
        'set_frame_area_offset':0.18,
        'set_frame_area':[0.2, 4.7],
        'set_tx_center_frequency':3,
        'set_prf_div':16,
        'set_fps':20}
    uwb = uwb_radar('COM3', args)
    # plt.ion()

    while True:
        try:
            if uwb.pure_data is not None:
                signal = uwb.pure_data[-20:, :]
                INPUT = tools.signal_energy(signal)
                amplitude, index, energy_ratio = tools.sp(INPUT, 15, 17)

                # plt.clf()
                # ax = np.arange(50, INPUT.shape[0]+50)/156+0.2
                # plt.plot(ax, INPUT, label='Smooth', color='b', marker="*")
                # plt.xlabel(xlabel='distance')
                # plt.ylabel(ylabel='energy')
                # plt.legend()
                # # plt.ylim((0, 1e-05))
                # plt.xlim((0, 5))
                # plt.xticks(np.arange(0, 5, 0.25))
                # plt.show()
                # plt.pause(0.5)

                # print('amplitude:', amplitude)
                # print('distance:', index)
                # print('energy_ratio:', energy_ratio)

                Person = 0
                Real = []
                for i in range(len(index)):
                    if(index[i]<=1.4):
                        if(amplitude[i] > 15.0e-07 and energy_ratio[i] > 0):
                            Person += 1
                            Real.append(index[i])

                    elif(index[i]>1.4 and index[i]<=2.4):
                        if (amplitude[i] > 4.0e-07 and energy_ratio[i] > 0):
                            Person += 1
                            Real.append(index[i])

                    elif (index[i] > 2.4 and index[i] <= 3.4):
                        if (amplitude[i] > 1.5e-07 and energy_ratio[i] > 0):
                            Person += 1
                            Real.append(index[i])

                    elif (index[i] > 3.4 ):
                        if (amplitude[i] > 0.7e-07 and energy_ratio[i] > 0):
                            Person += 1
                            Real.append(index[i])
                    else:
                        print("something wrong")
                list_men.append(Person)
                if(len(list_men)>5):
                    list_men.pop(0)
                Person=sum(list_men)//5
                save_json('Result.json', Person)
                print('-----------------------------------')
                print('当前人数:'+str(Person))
                print('位所在置:'+str(Real))

        except KeyboardInterrupt:
            uwb.reset()
            break
        except Exception:
            uwb.reset()
            print('Error detected. End radar!')
            break
        sleep(3)
