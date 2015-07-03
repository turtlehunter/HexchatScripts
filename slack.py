__module_name__ = 'Slacker'
__module_version__ = '0.1'
__module_description__ = 'Slack cleanup script'

import hexchat
from time import time
# hooks: "Channel DeVoice", "Channel Voice"
# emots: :grinning::grin::joy::smiley::smile::sweat_smile::satisfied::innocent::smiling_imp::wink::blush::yum::relieved::heart_eyes::sunglasses::smirk::neutral_face::expressionless::unamused::sweat::pensive:
#get's rid of voice notifications
def voice(word, word_eol, event, attrs):
	server = hexchat.get_info("network")
	if server == "Slack":
		return hexchat.EAT_ALL

hooks_voice = ["Channel DeVoice", "Channel Voice"]
for hook in hooks_voice:
	hexchat.hook_print_attrs(hook, voice, hook, hexchat.PRI_HIGH)
	
print("\00304" + __module_name__ + " successfully loaded.\003")
