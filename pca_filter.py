#-*-coding:utf-8 -*-
import scipy.io as sio
import numpy as np
from numpy import *
import os


def p_f(RawData,M,L):
    c=RawData.shape#数组维度
    FrameStitchnum=int(c[-1]/156)
    SpeedOfLight=3*10^8
    Resolution=0.006430041
    Fs=SpeedOfLight/(Resolution*2)
    #########带通滤波器##################
    BanFilter = [0.000858488568850877, -8.41769479099866e-05, 0.000181081091907345, -0.00101567371264779, -2.35075223972292e-05, 0.00376036114089048, -0.00487229031941366, -0.00198585766788643, 0.0105941427304610, -0.00774762405076410, -0.00578968761745269, 0.0120918646671639, -0.00376026966224768, -0.00170509279021220, -0.00625117332248972, 0.00408522379031234, 0.0267322754306968, -0.0467609025177357, -0.000231883860330190, 0.0833467784034521, -0.0879909718792097, -0.0295277434299727, 0.144160883670835, -0.0997984096490419, -0.0729924776161065, 0.170738114981189, -0.0729924776161065, -0.0997984096490419, 0.144160883670835, -0.0295277434299727, -0.0879909718792097, 0.0833467784034521, -0.000231883860330190, -0.0467609025177357, 0.0267322754306968, 0.00408522379031234, -0.00625117332248972, -0.00170509279021220, -0.00376026966224768, 0.0120918646671639, -0.00578968761745269, -0.00774762405076410, 0.0105941427304610, -0.00198585766788643, -0.00487229031941366, 0.00376036114089048, -2.35075223972292e-05, -0.00101567371264779, 0.000181081091907345, -8.41769479099866e-05, 0.000858488568850877]
    BanFilter2=np.array(BanFilter)
    BanFilter3=np.reshape(BanFilter2,[-1])


    #########带通滤波器##################
    batches=c[0]
    BandpassData=zeros((c[0],c[1]))
    ClutterData=zeros((c[0],c[1]))
    PureData=zeros((c[0],c[1]))
    pnum=76
    firnum=50
    alpha=0.9
    ####################################预处理######################################
    for raw in range(batches):
        for framenum in range(FrameStitchnum):
            blockdata=RawData[raw,(framenum)*pnum+1:min((framenum+1)*pnum,c[1])]
            blockmean=mean(blockdata)
            aa=blockdata.shape

            DCmean=np.ones((1,blockdata.shape[0]))*blockmean
            RawData[raw, (framenum) * pnum + 1:min((framenum + 1) * pnum, c[1])]=blockdata-DCmean

        convres=np.convolve(RawData[raw,:],BanFilter3)

        BandpassData[raw,:]=convres[int(firnum/2):int(firnum/2+c[1])]
        if raw==0:
            ClutterData[raw,:]=(1-alpha)*BandpassData[raw,:]
            PureData[raw,:]=BandpassData[raw,:]-ClutterData[raw,:]
        if raw>0:
            ClutterData[raw,:]=alpha*ClutterData[raw-1,:]+(1-alpha)*BandpassData[raw,:]
            PureData[raw,:]=BandpassData[raw,:]-ClutterData[raw,:]
    PureData=PureData[M:c[0],L:c[1]]

    return PureData









