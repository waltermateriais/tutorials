# -*- coding: utf-8 -*-
import cantera as ct


def sccm_to_meter_per_second(q, T_ref, P_ref, A_cross):
    """ Convert laboratory flow in SCCM to mean speed. """
    T_sccm = 273
    P_sccm = ct.one_atm
    scale = (T_ref / P_ref) * (P_sccm / T_sccm)

    min_per_sec = 1 / 60
    m3_per_cm3 = 1 / 10**6

    Q = q * min_per_sec * m3_per_cm3 * scale
    U = Q / A_cross
    
    return U
