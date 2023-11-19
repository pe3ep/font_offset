import json
from pathlib import Path
import os
import colorama
from colorama import Fore
colorama.init(autoreset=True)

font = input(f"{Fore.YELLOW}File path: {Fore.RESET}")
if os.path.exists(font):
  outdir = r'out/' 
  if not os.path.exists(outdir):
    os.makedirs(outdir)
  fileName = Path(font).stem

  print(f"{Fore.LIGHTBLACK_EX}-> {Fore.YELLOW}Editing {Fore.CYAN}{fileName}.json")
  print(f"{Fore.LIGHTBLACK_EX}Type {Fore.GREEN}exit {Fore.LIGHTBLACK_EX}to quit")

  while True:
    with open(font) as json_data:
      data = json.load(json_data)
    offset = input(f"{Fore.CYAN}Offset by: {Fore.RESET}")
    if offset == "exit":
      break
    else:
      offset = int(offset)
    newFileName = f"{str(fileName)}_offset_{str(offset)}"

    for item in data["providers"]:
      ascent = item["ascent"]
      ascent -= offset
      item["ascent"] = ascent

    with open("out/" + newFileName + ".json", "w") as newFile:
      json.dump(data, newFile, indent=2)
    print(f"{Fore.LIGHTBLACK_EX}-> {Fore.YELLOW}Created {Fore.GREEN}{newFileName}.json")
  print(f"{Fore.LIGHTBLACK_EX}-> {Fore.YELLOW}Made by {Fore.RED}Pe3ep")
else:
  print(f"{Fore.RED}File doesn't exist!")