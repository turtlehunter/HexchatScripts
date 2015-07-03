__module_name__ = 'Splitter'
__module_version__ = '0.3'
__module_description__ = 'Cleans up net split messages'
 
import hexchat
from time import time
 
split_timeout = 2 #time before split resets
last_split = time()
 
def split_finder(word, word_eol, event, attrs):
	
	global last_split
	reason = hexchat.strip(word[1])
	if reason == "*.net *.split":
		if time() - last_split > split_timeout:
			print("\00304IT'S A NET SPLIT!! RUN FOR THE HILLS")
			last_split = time()
		return hexchat.EAT_ALL
		
hook = "Quit"
hexchat.hook_print_attrs(hook, split_finder, hook, hexchat.PRI_HIGH)
print("\00304" + __module_name__ + " successfully loaded.\003")
