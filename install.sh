clear
apt install python python2 termux-api mpv figlet
pip install -U deep_translator
pip install datetime
pip install requests
rm $PREFIX/bin/termux-tts-speak
chmod +x termux-tts-speak
mv -v termux-tts-speak $PREFIX/bin/

mv -v assist $PREFIX/bin
chmod +x $PREFIX/bin/assist
clear
echo "Please subscribe our YT Channel -Dk Tech Point"
mkdir $PREFIX/ASSISTENT
mv -v * $PREFIX/ASSISTENT




