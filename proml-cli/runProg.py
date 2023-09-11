
"""Ce fichier contient une classe qui permet de manipuler un logiciel déja
existant à partir de la ligne de commande"""
import sys
import os
import time
import subprocess

class RunProg:

    def __init__(self, etat):
        self.__etat = etat

    def run_popen(self, cmd, logFile):
        duree = 0
        with open(logFile, "w") as f:
            if os.path.exists("./outfile"):
                os.remove("outfile")
            if os.path.exists("./outtree"):
                os.remove("outtree")
            p = subprocess.Popen([cmd], shell=True, stdout=f)
            print("\ndone.")

    def run(self):
        cmd="./proml< params.txt"
        self.run_popen(cmd, "log.txt")


    def read(self):

        if os.path.exists("./outfile"):
            p = subprocess.run('cat outfile', capture_output=True, text=True, shell=True)
            print("OUTFILE:\n")
            print(p.stdout)
        if os.path.exists("./outtree"):
            p = subprocess.run('cat outtree', capture_output=True, text=True, shell=True)
            print("OUTTREE:\n")
            print(p.stdout)

