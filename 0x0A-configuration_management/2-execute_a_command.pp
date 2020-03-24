# kills killmenow

exec { 'pkill -f killmenow":
  path => '/usr/bin:/usrlocal/bin:/bin'
}