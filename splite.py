import json
import sys

print ".--=============--=============--."
print "|       Welcome to Splite!       |"
print ".--=============--=============--."

yeswords = ["yes", "y", "ya", "ok", "okay"]

try:
    from PIL import Image
except:
    ans = raw_input("The Python Image Library is required to continue. Install it now? ")
    if ans.lower() in yeswords:
        try:
            os.system("sudo easy_install pip")
            os.system("sudo pip install Pillow")
        except:
            print("Install failed. Make sure you have a working gcc compiler")
            exit()
		
prev = []
try:
	f = open(".prev", "r")
	for line in f:
		prev.append(line)
	f.close()
except:
	pass

cur = open(".prev", "w")
cur_line = 0

def to_rgb(argb):
	return "".join(map(chr, argb)).encode('hex')

def sp_input(msg, default=""):
	global cur_line
	
	out = "| " + msg
	old = ""
	try:
		old += prev[cur_line].rstrip("\n")
	except:
		old = default
		
	if old != "":
		out += " [" + old + "]"
	
	out += ": "
	resp = raw_input(out)
	
	if resp == "":
		resp = old
		
	cur_line += 1
	cur.write(resp+"\n")
	
	return resp

try:
	sheet = sys.argv[1]
	print("| Using " + sheet)
except:
	sheet = raw_input("| Path to sprite sheet: ")
	
tile_width  = sp_input(" Width of tile")
tile_height = sp_input("Height of tile")

frames = sp_input(" Number of frames")
names  = sp_input("List of row names").replace(", ",",")

dirs = names.split(",")

#print ".--------------------------------"
#print("| Opening your sprite sheet...")

im = Image.open(sheet)
pix = im.convert('RGB')

offsetx = 0
offsety = 0

autobg = to_rgb(pix.getpixel((offsety, offsetx)))
truebg = sp_input("Background color", autobg)

print ".--------------------------------"
print "| I'm going to take " + sheet
print "| make " + str(len(dirs)) + " folders: " + str(dirs)
print "| representing iOS / OS X image sets"
print "| with " + str(frames) + " frames each"
print "| where every frame is " + str(tile_width) + "x" + str(tile_height)
print "| and remove the background color #" + truebg
print ".--------------------------------"
ans = raw_input("| Is this correct? ")

if not ans.lower() in yeswords:
	print("| I'm sorry to hear that :(")
	print ".--------------------------------"
	exit()
	
atlas_name = sp_input("Enter image atlas name")
print ".--------------------------------"

