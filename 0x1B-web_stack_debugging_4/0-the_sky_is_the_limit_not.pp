#fixed bugs in container
exec{ 'Update':
          command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
	  provider => shell,
}