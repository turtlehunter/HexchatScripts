__module_name__ = 'Name Colourer'
__module_version__ = '0.1'
__module_description__ = 'Colours names in chat messages using HexChat colouring'

import hexchat

#colour codes
colours = [ 19, 20, 22, 24, 25, 26, 27, 28, 29 ]

def colour_names(word, word_eol, event, attrs):
	
	
#get colour for name
def get_colour(name):
	raw = raw_input(name)
	sum = 0
	for ch in message:
		sum += ord(ch),
	return colours[sum % len(colours)]


#events to colour text
hooks = ["Your Message", "Channel Message", "Channel Msg Hilight", "Your Action", "Channel Action", "Channel Action Hilight"]

for hook in hooks:
	hexchat.hook_print_attrs(hook, colour_names, hexchat.PRI_HIGH)

print("\00304" + __module_name__ + " successfully loaded.\003")
