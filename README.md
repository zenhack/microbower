Bower solves a real problem, but needing node.js and npm for something 
that doesn't otherwise involve any server-side Javascript sucks. If 
you're interested in the event that motivated this tool, check out:

<http://zenhack.net/2015/06/06/openshift-bower-and-dependency-bloat.html>

What bower does isn't very complex. There's no reason I should need to 
pull in all that extra dependency bloat just to deploy my app.

MicroBower is a re-implementation of just enough of bower to fetch 
assets for a project, given that it already has a `bower.json` and 
`.bowerrc`. It's implemented in pure python, with no dependencies other 
git and the python standard library, and should work on python 2.7 or 
later (including python 3).

This is still WIP.
