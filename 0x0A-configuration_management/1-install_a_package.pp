exec {'install_flask_with_werkzeug':
  command => '/usr/bin/pip3 install flask==2.1.0 && /usr/bin/pip3 install werkzeug==2.1.1',
  path => ['/usr/bin', '/usr/bin'],
  unless => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
