#!/bin/bash


# Functions ----------

function start_music
{
	echo "Choose playlist for:" $1
	if [ "$1" = "neutral" ] || [ "$1" = "oops" ]; then
		echo "Play music for neutral/opps..."
		omxplayer -o local ./music/InMySecretLife.mp3 >/dev/null 
	elif [ "$1" = "happy" ]; then
		echo "Play music for happy..."
		omxplayer -o local ./music/Maroon5_Sugar.mp3 >/dev/null 
	elif [ "$1" = "sad" ] && [ "$2" = "0" ]; then
		echo "Play music for sad(close)..."
		omxplayer -o local ./music/Eminem_Lose_Yourself.mp3 >/dev/null 
	elif [ "$1" = "sad" ] && [ "$2" = "1" ]; then
		echo "Play music for sad(open)..."
		omxplayer -o local ./music/Adele_Hello.mp3 >/dev/null 
	elif [ "$1" = "angry" ]; then
		echo "Play music for angry..."
		omxplayer -o local ./music/Master_of_Puppets.mp3 >/dev/null 
	fi
	echo "End of the music"
}

function stop_music
{
	musicPID=$(ps | grep omxplayer | awk '{print $1}')
	echo $musicPID
	kill -9 $musicPID >/dev/null
}

# Functions ----------

while [ TRUE ]; do
	if [ -f "./mac" ]; then
		MACADDR=$(cat ./mac)
		echo "Already configured"
		break
	elif [ -f "./ip" ]; then
		echo "start configuration"
		IP=$(cat ./ip)
		MACADDR=$(arp -a | grep $IP | awk '{print $4}')
		MACADDR=${MACADDR^^}
		echo $IP
		echo $SUBNET
		echo $MACADDR
		echo $MACADDR > mac
		break
	else
		echo "Not config yet!"
		sleep 5
	fi
done


COUNT=0
STATE=0

IP=$(ip addr list eth0 |grep "inet " |cut -d' ' -f6|cut -d/ -f1)
echo "Shumei IP: " $IP
MACADDR=$(cat ./mac)
SUBNET="${IP%.*}.0"

while [ TRUE ]; do

RESULT=$(sudo nmap -sP $SUBNET/24 | grep $MACADDR)
echo "detecting..." $RESULT

if [ -z "$RESULT" ]; then
	echo "Device Not Found!" $COUNT
	if [ "$STATE" = "1" ]; then
		COUNT=$(($COUNT+1))
		if [ "$COUNT" = "5" ]; then
			STATE=0
			COUNT=0
			stop_music
			#echo "Stop music...."
		fi
	fi
else
	if [ "$STATE" = "0" ]; then
		echo $RESULT
		STATE=1
		COUNT=0
		USERID=$(cat ./id)
		PERSONALITY=$(cat ./personality | grep Creative)
		if [ -z "$PERSONALITY" ]; then
			# he/she is a close mind
			PERSONALITY=0
		else
			# he/she is a open mind
			PERSONALITY=1 
		fi
		
		MOOD=$(python twitter.py $USERID)
		
		#echo "Config:" $CONFIG
		echo "User ID:" $USERID
		echo "prefer:" $PERSONALITY
		echo "Mood:" $MOOD
		start_music $MOOD $PERSONALITY &
		#omxplayer ~/Music/InMySecretLife.mp3 &
		echo "Start playing Music ...."
		echo "State is:" $STATE
	else
		COUNT=0
		echo "Music is on ..."
		echo "State is:" $STATE
	fi
fi

sleep 5
done
