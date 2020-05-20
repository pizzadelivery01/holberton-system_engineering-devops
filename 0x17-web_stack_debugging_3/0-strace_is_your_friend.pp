# use this script to fix typo in config for holberton school debuging project

exec { 'fix typo in config':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }