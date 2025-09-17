import platform
from colorama import init, Fore
import pyfiglet
import os
import argparse

init(autoreset=True) 

parser = argparse.ArgumentParser(description="System Audit Tool")
parser.add_argument("--os", action="store_true", help="Check OS version")
parser.add_argument("--python", action="store_true", help="Check Python version")
parser.add_argument("--arch", action="store_true", help="Check system architecture")
parser.add_argument("--user", action="store_true", help="Check current user")
args = parser.parse_args()

if not any([args.os, args.python, args.arch, args.user]):
    args.os = args.python = args.arch = args.user = True

print(Fore.LIGHTBLUE_EX + pyfiglet.figlet_format("System Audit", font="slant"))


os_name = platform.system()
os_version = platform.version()
architecture = platform.architecture()[0]
machine_type = platform.machine()
processor = platform.processor()
python_version = platform.python_version()
python_compiler = platform.python_compiler()
computer_name = platform.node()
current_user = os.getlogin()

if args.os:
  print(Fore.CYAN + "OS:", os_name, os_version)

if args.arch:
 print(Fore.CYAN + "Architecture:", architecture)
 print(Fore.CYAN + "Machine Type:", machine_type)
 print(Fore.CYAN + "Processor:", processor)

if args.python:
 print(Fore.CYAN + "Python Version:", python_version)
 print(Fore.CYAN + "Python Compiler:", python_compiler)

if args.user:
 print(Fore.CYAN + "Computer Name:", computer_name)
 print(Fore.CYAN + "Current User:", current_user)

issues = []

if args.os:
 if os_name == "Windows" and os_version.startswith("6.1"):
    issues.append(Fore.RED + "Old Windows version detected (Not safe)")

if args.arch:
 if architecture != "64bit":
    issues.append(Fore.RED + "Non-64bit architecture detected (Not safe)")
 if not processor:
    issues.append(Fore.RED + "Unknown processor type (Not safe)")

if args.python:
 major, minor, *_ = map(int, python_version.split('.'))
 if major == 3 and minor < 10:
    issues.append(Fore.RED + "Old Python version detected (Not safe)")

if args.user:
   if not current_user or current_user.lower() == "guest":
    issues.append(Fore.RED + "Current user is 'guest' or unknown (Not safe)")

with open("audit_report.txt", "w", encoding="utf-8") as f:
  f.write("System Audit Report\n")
  f.write("===================\n")
  f.write(f"OS: {os_name} {os_version}\n")
  f.write(f"Python: {python_version}\n")
  
  
if not issues:
    print(Fore.GREEN + "No issues detected. System is secure.")
else:
    print(Fore.RED + "Potential issues detected:")
    for issue in issues:
        print(Fore.RED + "- " + issue)