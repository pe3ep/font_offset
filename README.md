# Minecraft font offset

`Python tool to create font offset by the specified amount of pixels`

---

### Usage:

```bash
# Clone the repository
git clone https://github.com/pe3ep/font_offset.git # Or download source code
cd font_offset/

# Install dependencies
pip install -r requirements.txt

# Use tool
python main.py
```

```py
File path: test/test.json # Original file
-> Editing test.json
# Amount of pixels that need to be offset.
# offset > 0 - sprite moves down
# offset < 0 - offset moves up
Offset by: 3
-> Created test_offset_3.json
...
```
