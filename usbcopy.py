#!/usr/bin/python

# python script for Linux to copy data onto masses of USB pendrives (e.g. for conference proceedings)
#
# listens to DBUS event of when pendrive is mounted,
# automatically copies given files to pendrive,
# then unmounts and renames volume to given name
#
# TODO: get device name from mount,
# verify pendrive somehow,
# format if needed/delete current files

SRC="/home/marco/Downloads/EUNICE_USB/*"
DEV="/dev/sdc1"
VOLUMENAME="EUNICE2013"

import dbus
import gobject
import dbus.mainloop.glib
import os
import urlparse
import urllib

def handler(*args, **kwargs):
	if not kwargs["member"] == "MountAdded":
		#print kwargs["member"]
		#print args
		return

	print "--- USB device mounted ---"
	#print args
	#print "mount path: ", args[2][5]

#	take argument with url string, turn file://... into path
	url=urlparse.urlparse(args[2][5]).path
#	turn %20 into spaces
	path = urllib.unquote(url).decode('utf8')
#	add quotation marks
	path = '"%s"' % path

	print "copying..."
	os.system("cp -r %s %s" % (SRC, path))
	os.system("sync")
	
	os.system("umount %s" % path)
#	use fixed path for now -> just one pendrive at a time
	os.system("sudo mlabel -i %s ::%s" % (DEV, VOLUMENAME))
	print "done. insert next pendrive or stop with Ctrl-c"


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
bus.add_signal_receiver(handler,interface_keyword="dbus_interface",member_keyword="member")

loop = gobject.MainLoop()
loop.run()
