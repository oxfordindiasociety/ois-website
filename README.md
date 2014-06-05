# Oxford India Society website source

The website is generated using [Hakyll](http://jaspervdj.be/hakyll/).

The website can be updated by doing the following at the command line:
    $ ghc site.hs
    $ ./site build && ./site deploy
(after cloning the repository).

Posts are in the `posts/` directory, mostly they are just metadata about
the event in YAML format.

The theming is using Bootstrap with the Readability theme.

