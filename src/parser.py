#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:04:30 2026

@author: MatiasGamezMarin
"""
def parse_line(line: str):
    parts = line.split()
    if len(parts) < 10:
        raise ValueError("Malformed line")
        
    
    timestamp = float(parts[0])
    header_response = int(parts[1])
    ip = parts[2]
    try:
        http_response = int(parts[3].split("/")[1])
    except (IndexError, ValueError):
        print("Malformed http_response")
    
    bytes_size = int(parts[4])
    http_request = parts[5]
    url = parts[6]
    username = parts[7]
    destination_ip = parts[8]
    response_type = parts[9]
    
    return {
        "timestamp" : timestamp,
        "header_response" : header_response,
        "IP" : ip,
        "http_response" : http_response,
        "bytes_size" : bytes_size,
        "http_request" : http_request,
        "URL" : url,
        "Username" : username,
        "IP_destination" : destination_ip,
        "Response_type" : response_type
        }
