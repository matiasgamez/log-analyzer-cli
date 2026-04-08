#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:08:17 2026

@author: MatiasGamezMarin
"""
def ip_count(data):  
    N_ip = {}
    for d_line in data:
        ip_i = d_line['IP']
        N_ip[ip_i] = N_ip.get(ip_i,0) + 1
    return N_ip
    
def eps_count(data):
    eps = {}
    for d_line in data:
        sec = int(d_line['timestamp'])
        eps[sec] = eps.get(sec,0) + 1
    return eps

def total_bytes(data):
    return sum(d_line['bytes_size'] for d_line in data)

def most_frequent_ip(ip_counts):
    return max(ip_counts,key=ip_counts.get)

def least_frequent_ip(ip_counts):
    return min(ip_counts,key=ip_counts.get)
