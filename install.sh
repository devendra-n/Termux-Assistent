clear
apt install python python2 git screenfetch ruby termux-api mpv figlet
pip install -U deep_translator
gem install lolcat
pip install wikipedia
pip install datetime
pip install requests
pip install wikipedia
pip install instaloader
rm $PREFIX/bin/termux-tts-speak
chmod +x termux-tts-speak
mv -v termux-tts-speak $PREFIX/bin/

mv -v assist $PREFIX/bin
chmod +x $PREFIX/bin/assist
clear
echo "Please subscribe our YT Channel -Dk Tech Point" |lolcat -a
mkdir $PREFIX/.ASSISTENT
mv -v * .ASSISTENT




