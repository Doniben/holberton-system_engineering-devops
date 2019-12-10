# Using Puppet, create a manifest that kills a process

exec { 'kill':
  command  => 'pkill killmenow',
  provider => 'shell'
}