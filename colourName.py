__module_name__ = 'Name Colourer'
__module_version__ = '0.5'
__module_description__ = 'Colours names in chat messages using HexChat colouring'

import hexchat
import re

#colour codes
colours = [ 19, 20, 22, 24, 25, 26, 27, 28, 29 ]
#valid name pattern
name_start = "a-zA-Z_\-\[\]\\\^{}|`"
name_other = "0-9" + name_start

halt = False

def colour_names(word, word_eol, event, attrs):
	
	global halt, name_start, name_other
	
	if halt:
		return
	
	users = hexchat.get_list("users")
	message = word[1]
	
	for user in users:
		if re.search(('(?!' + name_start + ')%s(?!=' + name_other + ')') % (user), message):
			colour = get_colour(user)
			message = re.sub(r'((?!' + name_start + '))(%s)((?!=' + name_other + '))' % (user),r'\1\\003' + colour + user + '\\003\3', message)
	word[1] = message
	halt = True
	hexchat.emit_print(event, *word)
	halt = False
	return hexchat.EAT_ALL
	
#get colour for name
def get_colour(name):
	
	global colours
	raw = raw_input(name)
	total = 0
	for ch in message:
		total += ord(ch)
	return colours[total % len(colours)]


#events to colour text
hooks = ["Your Message", "Channel Message", "Channel Msg Hilight", "Your Action", "Channel Action", "Channel Action Hilight"]

for hook in hooks:
	hexchat.hook_print_attrs(hook, colour_names, hexchat.PRI_HIGH)

print("\00304" + __module_name__ + " successfully loaded.\003")
