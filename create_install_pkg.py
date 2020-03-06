import time
import os
import shutil

import subprocess
import platform

def execute_shell(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def cleaning_before_commit():

	files="""
build
dist
cvmodels/__pycache__
"""
	print("Cleaning files -",files)

	files = files.split('\n')

	for file in files:
		if os.path.exists(file):
			try:
				shutil.rmtree(file)
			except:
				os.remove(file)




if __name__ == '__main__':
	if platform.system() == 'Linux':
		commands = """pip3 uninstall cvmodels -y
python3 setup.py sdist bdist_wheel
python3 setup.py install"""
	elif platform.system() == 'Windows':
		commands = """pip3 uninstall cvmodels -y
python setup.py sdist bdist_wheel
python setup.py install"""


	commands = commands.split("\n")

	for command in commands:
		for path in execute_shell(command):
		    print(path, end="")

	cleaning_before_commit()