
# robustness

* [ ] reasonable error checking
  * [x] check files for correctness
  * [ ] check network request responses

# .bowerrc support

## probably should support

* [ ] cwd
* [x] directory
  * [x] default to saving things in `bower_components`
  * [x] if specified, save components in this directory.

## nice to have, but low priority

* [ ] registry
* [ ] proxy
* [ ] https-proxy
* [ ] user-agent (should default to something specifying microbower).
* [ ] timeout
* [ ] strict-ssl
* [ ] ca

## Can probably ignore

* [ ] analytics (off by default, we don't need to turn it on)
* [ ] color
* [ ] interactive (the whole point is for server-side deployment; we
  probably never want this).

## Not necessarily meaningful; concerns implementation:

* [ ] storage
* [ ] tmp

# bower.json support

## probably should support

* [ ] dependencies
  * [x] scan names of packages
  * [ ] make use of version/path info (right now we just query the
    registry and get master, or give up).

## nice to have, but low priority

* [ ] main
* [ ] ignore

(avoids pulling in extra files --- will still work if we don't take
advantage).

* [ ] devDependencies

(not used for production mode, which is what we're mainly interested
in).
'r
## Can probably ignore

* [ ] name
* [ ] semver
* [ ] keywords
* [ ] private

(These are all probably only interesting if you're publishing your
package, which is not what microbower is for).
