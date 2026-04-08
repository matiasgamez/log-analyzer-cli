#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:09:57 2026

@author: MatiasGamezMarin
"""
import argparse
from parser import parse_line
from functions import *
import json

def main():
    parser = argparse.ArgumentParser()
    
    ## Required argument ##    
    parser.add_argument(
        "--input",
        required=True,
        help="Path to one or more input files"
    )
    
    parser.add_argument("--output",
                        type = str,
                        required = True,
                        help = "Path to output file (JSON format)")

    ## Optional arguments ##
    parser.add_argument(
        "--mfip",
        action="store_true",
        help="Most frequent IP"
    )
    
    parser.add_argument(
        "--lfip",
        action="store_true",
        help="Least frequent IP"
    )
    
    parser.add_argument(
        "--eps",
        action="store_true",
        help="Events per second"
    )
    
    parser.add_argument(
        "--bytes",
        action="store_true",
        help="Total bytes exchanged"
    )
    
    args = parser.parse_args()

    ################################
    
    data_list = []
    file_name = args.input
    with open(file_name,"r") as f:
        for line in f:
            try:
                data = parse_line(line)
                data_list.append(data)
            except ValueError:
                continue
                #########################
                

    N_ip = ip_count(data_list)    
    eps = eps_count(data_list)
    
    results = {}
    if args.mfip and N_ip:
        max_ip = most_frequent_ip(N_ip)
        print(f"Most frequent IP: {str(max_ip)}. Count: {N_ip[max_ip]}")
        results["most_frequent_ip"] = {
            'ip' : max_ip,
            'counts' : N_ip[max_ip]}
    
    if args.lfip and N_ip:
        least_ip = least_frequent_ip(N_ip)
        print(f"Least frequent IP: {least_ip}. Count: {N_ip[least_ip]}")
        results["least_frequent_ip"] = {
            'ip' : least_ip,
            'counts' : N_ip[least_ip]}
    
    if args.bytes:
        total = total_bytes(data_list)
        print(f"Total amount of bytes exchanged: {total}")
        results["total_bytes"] = total
        
    if args.eps and eps:
        results["events_per_second"] = eps
        print(eps)
        
    if not any([args.mfip, args.lfip, args.bytes, args.eps]):
        print('No operation specified. Use --help for options')
            
    with open(args.output,"w") as f:
        json.dump(results, f, indent=4)

             
if __name__ == "__main__":
    main()
    

        
