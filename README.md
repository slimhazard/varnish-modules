# About this repository

This repository is based upon
https://github.com/varnish/varnish-modules with additions and
necessary adjustments for varnish-cache master. It is being maintained
by https://uplex.de/

Included:

* `bodyaccess`: Client request body access
* `header`:Modify and change complex HTTP headers
* `saintmode`: 3.0-style saint mode
* `str`: String operations
* `tcp`: TCP connections tweaking
* `var`: Variable support
* `vstrottle`: Request and bandwidth throttling
* `xkey`: Advanced cache invalidations

# Upstream notes

Modules in this repository are generally not in active development by
Varnish Software. However, any security related bugs and issues will
always be a high priority. We'll also gladly considering pull requests for new
features but we recommend opening an issue first to discuss implementation
plans.

## Usage

Each module has a different set of functions and usage, described in
separate documents in `docs/`. For completeness, here is a snippet from
`docs/cookie.rst`::

    import cookie;

    sub vcl_recv {
            cookie.parse(req.http.cookie);
            cookie.filter_except("SESSIONID,PHPSESSID");
            set req.http.cookie = cookie.get_string();
            # Only SESSIONID and PHPSESSID are left in req.http.cookie at this point.
    }


## Moved or replaced VMODs

VMODs in this category are no longer maintained because their
functionality is covered by other functionality or newer VMODs.

In this repository there is only two such vmods:

* ``cookie``, that is now part of Varnish.

* ``softpurge`` is now replaced by the ``purge`` VMOD in Varnish.
  Note that this VMOD is also in the "feature complete" category,
  since it is still needed for Varnish Cache 4.1.

## Administrativa

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


## Contact

This code is maintained by Varnish Software. (https://www.varnish-software.com/)

Issues can be reported via the Github issue tracker.

Other inquires can be sent to opensource@__no_spam_please__varnish-software.com.

