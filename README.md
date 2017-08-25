# pobad

For when you absolutely, positively have to write Rust code in Python in your phone.

This is pretty much a Python port of @badboy's [poor-mans-rust-full.sh](https://gist.github.com/badboy/f0068cefb7e41e3ec2eb) script. 

The general gist (see what I did there) of the code is to call the [Rust playground's](https://play.rust-lang.org) `/evaluate.json` end point with your code. So yes, you will need internet connectivity.

I've tested this on python 3.5.1 ([Pythonista3](http://omz-software.com/pythonista/docs/)) and 3.6.2 (MacOS).

![Rust via Pythonista3](https://raw.githubusercontent.com/booyaa/pobad/master/images/pythonista.jpg)

# Installation

The only python module you need is [requests](http://docs.python-requests.org/en/master/).

You can either install this directly (yolo) or within a virtual environment.

# Usage

`./pobad.py rust_file`

If you do plan on using this in Pythonista, then I recommend you also install [StaSh](https://github.com/ywangd/stash). StaSh is an incredibly useful shell that will allow you to upload the pobad script onto your iPhone and then execute in a similar manner to example below.

# Licensing

- [Apache v2](LICENSE)

# Copyright

The original copyright should go to Jan-Erik Rediger (@badboy). I guess I could take credit for the python port.

Mark Sta Ana 2017 &copy;