#!/usr/bin/env python

'''This demonstrates an FTP "bookmark". This connects to an ftp site; does a
few ftp stuff; and then gives the user interactive control over the session. In
this case the "bookmark" is to a directory on the OpenBSD ftp server. It puts
you in the i386 packages directory. You can easily modify this for other sites.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>, Modified 2018 Jean-Bernard Addor
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

'''

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import sys

# Note that, for Python 3 compatibility reasons, we are using spawnu and
# importing unicode_literals (above). spawnu accepts Unicode input and
# unicode_literals makes all string literals in this script Unicode by default.
# child = pexpect.spawnu('cadaver http://localhost:8000')
child = pexpect.spawn('cadaver')
# child.logfile = sys.stdout
child.logfile_read = sys.stdout
child.expect('dav:!> ')
child.sendline('help')
child.expect('dav:!> ')
child.sendline('unset quiet')
child.expect('dav:!> ')
child.sendline('open http://localhost:8000')
child.expect('Username: ')
child.sendline('user')
child.expect('Password: ')
child.sendline('user')
child.expect('dav:.* ')
child.sendline('pwd')
child.expect('dav:.* ')
child.sendline('put LICENSE')
child.expect('dav:.* ')
child.sendline('put README.md')
child.expect('dav:.* ')
child.sendline('put server.php')
child.expect('dav:.* ')
child.sendline('get LICENSE /dev/null')
child.expect('dav:.* ')
child.sendline('get README.md /dev/null')
child.expect('dav:.* ')
child.sendline('get server.php /dev/null')
child.expect('dav:.* ')
child.sendline('delete server.php')
child.expect('dav:.* ')
# sys.stdout.write (child.before)
# print("Escape character is '^]'.\n")
# sys.stdout.write (child.after)
# sys.stdout.flush()
# child.interact(escape_character='!') # Is there a way to use it in Travis? (It seems not to take piped input.)
# Escape character defaults to ^]
# At this point this script blocks until the user presses the escape character
# or until the child exits. The human user and the child should be talking
# to each other now.

# At this point the script is running again.
# print('Left interactve mode.')

# The rest is not strictly necessary. This just demonstrates a few functions.
# This makes sure the child is dead; although it would be killed when Python exits.
if child.isalive():
    child.sendline('quit') # Try to ask cadaver child to exit.
    child.expect(pexpect.EOF)
    # print(child.before)
    child.close()
# Print the final state of the child. Normally isalive() should be FALSE.
if child.isalive():
    print('Child did not exit gracefully.')
else:
    print('Child exited gracefully.')
print(child.exitstatus, child.signalstatus)

