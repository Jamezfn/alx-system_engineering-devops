#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package {'python::pip':
  name => 'flask',
  pkgname => 'flask'
  ensure   => '2.1.0',
  pip_provider => 'pip3'
}
