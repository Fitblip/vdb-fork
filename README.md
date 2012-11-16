VDB-fork
========

A fork of @invisig0th's VDB, for bugfixes, and other stuff. 

I'm going to attempt to fix a bug or two I've stumbled across, and maybe come up with some tests for VDB. 
                                          
===== Intro  ===================================================

VDB is a debugger written using the vtrace API.  For the list
of kewl stuff and supported features, see the vtrace docs.


===== Usage  ===================================================

I usually run it directly from the checkout without going through
any kind of installation.  From a windows/unix command prompt,
"python vdbbin" should suffice.

If you want to use the gui (on mac/linux/windows) you will need
a working install of pygtk (which means gtk/pango/etc).

I'm not really one for writting a LOT of docs, but explore and have fun.


===== Known Iusses  ============================================

 * -R and firewalls
    Remove debugging with vdb is possible with the use of the
    "server" command and the -R option.  *However*, cobra
    (the underlying RMI model) will attempt transparent reconnection
    for robustness.  This means that firewalls can cause it to hang
    as it tries to reconnect.  This also means that one socket dying
    once doesn't destroy your debugging session ;)

 * NonBlocking or ThreadWrap modes
    Though these modes are listed in the modes selection interface
    you may *not* turn them off.  They are critical to the function
    of vdb as a non-blocking debugger...

