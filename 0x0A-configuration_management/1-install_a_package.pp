# using puppet  install flask 2.1.0 from pip3 package
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
