Status of this repository
=========================

This repository is based upon
https://github.com/varnish/varnish-modules with necessary adjustments
for varnish-cache master. It is being maintained by https://uplex.de/

Varnish module collection by Varnish Software
=============================================

This is a collection of modules ("vmods") extending Varnish VCL used for
describing HTTP request/response policies with additional capabilities.

Included:

* Variable support
* Request and bandwidth throttling
* Modify and change complex HTTP headers
* 3.0-style saint mode,
* Advanced cache invalidations, and more.
* Client request body access

This collection contains the following vmods (previously kept
individually): vsthrottle, header, saintmode, softpurge, tcp, var,
xkey, bodyaccess

Supported Varnish version is described in the `CHANGES.rst` file. Normally this
is the last public Varnish Cache release. See PORTING below for information on
support for other versions of Varnish.


Installation
------------

Source releases can be downloaded from:

    https://download.varnish-software.com/varnish-modules/


Installation requires an installed version of Varnish Cache, including the
development files. Requirements can be found in the `Varnish documentation`_.

.. _`Varnish documentation`: https://www.varnish-cache.org/docs/4.1/installation/install.html#compiling-varnish-from-source
.. _`Varnish Project packages`: https://www.varnish-cache.org/releases/index.html


Source code is built with autotools, you need to install the correct development packages first.
If you are using the official `Varnish Project packages`_::

    sudo apt-get install varnish-dev || sudo yum install varnish-devel

If you are using the distro provided packages::

    sudo apt-get install libvarnishapi-dev || sudo yum install varnish-libs-devel

Then proceed to the configure and build::

    ./configure
    make
    make check   # optional
    sudo make install


The resulting loadable modules (``libvmod_*.so`` files) will be installed to
the Varnish module directory. (default `/usr/lib/varnish/vmods/`)


Usage
-----

Each module has a different set of functions and usage, described in
separate documents in `docs/`. For completeness, here is a snippet from
`docs/header.rst`::

    vcl 4.0;
    import header;

    backend default { .host = "192.0.2.11"; .port = "8080"; }

    sub vcl_backend_response {
        if (beresp.http.Set-Cookie) {
            # Add another line of Set-Cookie in the response.
            header.append(beresp.http.Set-Cookie, "VSESS=abbabeef");

            # CMS always set this, but doesn't really need it.
            header.remove(beresp.http.Set-Cookie, "JSESSIONID=");
        }
    }



Development
-----------

The source git tree lives on Github: https://github.com/varnish/varnish-modules

All source code is placed in the master git branch. Pull requests and issue
reporting are appreciated.

Unlike building from releases, you need to first bootstrap the build system
when you work from git::

    ./bootstrap
    ./configure
    make
    make check # recommended

If the ``configure`` step succeeds but the ``make`` step fails, check for
warnings in the ``./configure`` output or the ``config.log`` file. You may be
missing bootstrap dependencies not required by release archives.

Porting
-------

We encourage porting of the module package to other versions of Varnish Cache.


Administrativa
--------------

The goals of this collection are:

* Simplify access to vmod code for Varnish users. One package to install, not 6.
* Decrease the maintenance cost that comes with having 10 different git
  repositories, each with autotools and (previously) distribution packaging files.

Expressed non-goals are:

* Import vmods that require external libraries, like curl or geoip. This
  collection should be simple and maintenance free to run.
* Support older releases of Varnish Cache.
* Include every vmod under the sun. We'll add the important ones.

Addition of further vmods is decided on a case-by-case basis. Code quality and
maintenance requirements will be important in this decision.


Contact
-------

This code is maintained by Varnish Software. (https://www.varnish-software.com/)

Issues can be reported via the Github issue tracker.

Other inquires can be sent to opensource@__no_spam_please__varnish-software.com.

