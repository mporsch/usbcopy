usbcopy
=======

python script for Linux to copy data onto masses of USB pendrives (e.g. for conference proceedings)

listens to DBUS event of when pendrive is mounted,
automatically copies given files to pendrive,
then unmounts and renames volume to given name

TODO: get device name from mount,
verify pendrive somehow,
format if needed/delete current files
