import json
from pathlib import Path
import os

font = input("File path: ")
if os.path.exists(font):
  outdir = r'out/' 
  if not os.path.exists(outdir):
    os.makedirs(outdir)
  fileName = Path(font).stem

  print("-> Editing " + fileName + ".json")

  while True:
    with open(font) as json_data:
      data = json.load(json_data)
    offset = int(input("Offset by: "))
    newFileName = str(fileName) + "_offset_" + str(offset)

    for item in data["providers"]:
      ascent = item["ascent"]
      ascent -= offset
      item["ascent"] = ascent

    with open("out/" + newFileName + ".json", "w") as newFile:
      json.dump(data, newFile, indent=2)
    print("-> Created " + newFileName + ".json")
else:
  print("File doesn't exist")