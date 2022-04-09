How to use the GUI API:

	First import the API using the 'from GUI_API import API as api'. From there you will have access
to the GUI API functions. These functions include the ablility to make windows and add buttons, labels, icons
and images to those windows. Below is the terminolagy on how to properly use the API and what commands get you
the different looks of tkinkter. The purpose of this API is to allow a person to still use the amazing feactures
of tkinter but now with the abillity to make your base code easier to read.


New Varibles:

	To create a new window or other object in tkinter using the API you must first assign the attributes of
that object to a varible. The reason for this is the API is built off a package system. A package is used to take
all the objects you wish to put on a window and send it as on attribute to the API. The API then uses this package 
that you send it and identifys weather or not the object is a window, button, label, icon, or image and then applies
