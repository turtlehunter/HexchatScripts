# HexchatScripts
Python scripts for IRC chat client Hexchat

Current IRC scripts include:

## Filter 2
An adaptation of the [Smart Filter](https://github.com/hexchat/hexchat-addons/tree/master/python/smart_filter), it removes join and part (quit) messages from chat, unless the user has spoken.

## Split
A filter to remove `*.net *.split` part messages from chat, which can occur when a server on an IRC network is disconnected, and the users hosted there are ejected.

## Slack
A script to improve the usability of [Slack](https://slack.com) communication via IRC. Currently only removes voice and devoice messages.
