# -*- coding: utf-8 -*-
BASE_SIGNAL=10000
END_SIGNAL=BASE_SIGNAL+1000

NO_DONGLES		=BASE_SIGNAL+0
DONGLES_ADDED		=BASE_SIGNAL+1
CYCLE_SDK_DONGLE	=BASE_SIGNAL+2

TOO_BUSY		=BASE_SIGNAL+10

CONNECTED		=BASE_SIGNAL+100
CONNECTION_FAILED	=BASE_SIGNAL+101

HANDLED_OK		=BASE_SIGNAL+200
HANDLED_LOST_CONNECTION	=BASE_SIGNAL+201
HANDLED_HISTORY		=BASE_SIGNAL+202

TEXT={
    NO_DONGLES: 'NO_DONGLES',
    DONGLES_ADDED: 'DONGLES_ADDED',
    CYCLE_SDK_DONGLE: 'CYCLE_SDK_DONGLE',
    TOO_BUSY: 'TOO_BUSY',
    CONNECTED: 'CONNECTED',
    CONNECTION_FAILED: 'CONNECTION_FAILED',
    HANDLED_OK: 'HANDLED_OK',
    HANDLED_LOST_CONNECTION: 'HANDLED_LOST_CONNECTION',
    HANDLED_HISTORY: 'HANDLED_HISTORY',
}

def isSensorSDKSignal(val):
    return val >= BASE_SIGNAL and val <= END_SIGNAL