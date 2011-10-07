Directional "Duplicate Line" for Sublime Text 2
===============================================

This plugin adds a directional "Duplicate Line" command. You can duplicate lines and selections either "up" (before current line/selection) or "down" (after, which is the default `duplicate_line` behavior).


Motivation
----------

As many other simple text editor plugins, this one comes from a desire to make the new editor behave more like another one. I liked [Eclipse](http://eclipse.org/)'s duplicate line functionality. You press `ctrl+alt+up` / `ctrl+alt+down` (`command` and `option` on macs) and it duplicates the line you're on, either up or down.


Is it any good?
---------------

[Yes](http://news.ycombinator.com/item?id=3067434).


Installation
------------

Copy the application folder into Sublime's `Packages` folder. That's it.


Usage
-----

You have to bind the commands to keys. This is what I did (on a mac, trying to mimic Eclipse's bindings):

    { "keys": ["super+alt+up"], "command": "directional_duplicate_line", "args": {"direction": 1} },
    { "keys": ["super+alt+down"], "command": "directional_duplicate_line", "args": {"direction": 0} },
 

* Now, `command+shift+down` will behave like the regular `duplicate_line` (usually `command+shift+d`) and, well, duplicate your line. Or selection.

* `command+shift+up` will duplicate your lines "up", which actually means duplicating it regularly but keeping the cursor where it is. Same for selections.


Limitations
-----------

Behavior with multiple selection seems kind of weird sometimes, but is consistent with the original `duplicate_line` command.


Acknowledgements
----------------

Thanks to the guys who wrote the awesome [Sublime Text 2](http://www.sublimetext.com/2).  
Also, thanks to whoever wrote [http://www.sublimetext.info/]() and the original `duplicate_line` script.  
And thanks to [Alexander Staubo](https://github.com/alexstaubo/), who wrote the [sublime_text_alternative_autocompletion](https://github.com/alexstaubo/sublime_text_alternative_autocompletion) plugin, from which this Readme's structure is blatantly copied.


License
-------

Copyright 2011 Marcelo Alvim. MIT license. See `LICENSE` file for license.
