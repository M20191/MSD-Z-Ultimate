#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Create by M20191

# Import modules
import os
import argparse
import platform
import re
from mcstatus import MinecraftServer
from datetime import datetime
from typing import Any


def get_os(args:dict[str:str]) -> str:
	"""Recon Mode, get OS of server

	Args:
		args (dict[str:str]): Args command line

	Returns:
		str: OS | TTL
	"""
	# Recon OS exectscript
	system = platform.system()

	if system == "Windows":
		# Run command
		cmd = os.system(f'ping -nl 1 {args.host} | find /I "TTL" > ttl.tmp')
		ttl = open('ttl.tmp','r').read().split(" ")[-1]
		# Remove tmp ping ttl
		os.system("del ttl.tmp")
		
		if int(ttl.split("=")[1]) <= 64:
			return f"OS: Linux | {ttl}"
		
		return f"OS: Windows | {ttl}"

	# Else platform Linux
	# Beta


def server(server_name: str) -> dict[str:str]:
	"""
	Returns a object in which we can extract information from server pinged.\n
	Args:\n
		* server_name (str): minecraft server IP/DNS

	Returns:\n
		* response (object): returns a object to which information is extracted
	"""
	# Ping function return 0 if server don´t response
	try:
		server_ping = MinecraftServer.lookup(server_name)
		return server_ping.status()

	except:return 0
		
def information_server():
	"""
	Main function printing server information
	"""
	# Initialize parser
	parser = argparse.ArgumentParser()
	
	# Adding optional argument
	parser.add_argument("-ip", "--host", help="Ip address to connsult data", type=str)
	parser.add_argument("-o", "--outfile", help="Outfile to saved ping data", type=str)
	parser.add_argument("-r", "--recon", help="Return the OS of server",action="store_true")
	# Read arguments from command line
	args = parser.parse_args()

	# Get name of server
	info_server = server(args.host)

	# server error
	if info_server==0 or args.host == None:print("Error server ping | [!] python ping_server.py -ip mc.hypixel.net");exit()

	# Information of server
	information_server = {
		"Time to ping":datetime.now(),
		"Ip":args.host,
		"Port":info_server.version.protocol,
		"Players":info_server.players.online,
		"Max/Players":info_server.players.max,
		"Availability":info_server.players.max - info_server.players.online,
		"Latency":str(info_server.latency).split(".")[0],
		"Version/Bunge":info_server.version.name[0:15]+" "+info_server.version.name[-6:],
		"Description":re.sub('§[\da-zA-Z]', '', info_server.description),
		"Status":"Active"
	}

	# items of information_server
	for i,x in information_server.items():
		print(f'{i}: {x}')

	# Save into a log file
	if args.outfile:
		with open(args.outfile,"w", encoding='utf-8') as w:w.write('\n'.join(f"{xd[0]} {xd[1]}" for xd in ([i,x] for i, x in information_server.items())))

	# Print OS
	if args.recon:
		print(get_os(args))
# Core
if __name__ == '__main__':
	# Main
	information_server()