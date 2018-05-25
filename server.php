<?php

use Sabre\DAV;
use Sabre\DAV\Auth;

require 'vendor/autoload.php';

$server = new DAV\Server(new DAV\FS\Directory('public'));
$server->setBaseUri('/');
$server->addPlugin(new DAV\Locks\Plugin(new DAV\Locks\Backend\File('data/locks')));
$server->addPlugin(new DAV\Browser\Plugin());
$server->addPlugin(new DAV\Sync\Plugin());

$authBackend = new Auth\Backend\File('htdigest');
$authBackend->setRealm('SabreDAV');
$server->addPlugin(new Auth\Plugin($authBackend));
# $server->addPlugin(((new Auth\Backend\File('htdigest'))->setRealm('SabreDAV'))); # Seems not to work.

$server->exec();

// from: http://sabre.io/dav/gettingstarted/
