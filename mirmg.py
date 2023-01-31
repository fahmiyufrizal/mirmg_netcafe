# mirm simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
from sys import exit
import asyncio
import pathlib

print("[+] Launching MirM Global Launcher....")
async def display():
	await asyncio.sleep(5)
asyncio.run(display())
os.system('start "" launcher\MirMGLauncher.exe')