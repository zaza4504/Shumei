<?php
if( isset($_POST['demo']) && isset($_POST['TwitterAccount']) ) {
    $id = $_POST['TwitterAccount'] . "\n";
    $personality = $_POST['demo'] . "\n";
    $ip = $_SERVER['REMOTE_ADDR'] . "\n";

    echo "Your personality:  {$personality} <br><br>";
    $ret = file_put_contents('/home/pi/Projects/IoT/id', $id, LOCK_EX);
    if($ret === false) {
        die('There was an error writing id file');
    }   
    else {
        echo "Save your Twitter ID<br>";
    }
   
    $ret = file_put_contents('/home/pi/Projects/IoT/personality', $personality, LOCK_EX);
    if($ret === false) {
        die('There was an error writing personality file');
    }   
    else {
        echo "Save your personality<br>";
    }   

    $ret = file_put_contents('/home/pi/Projects/IoT/ip', $ip, LOCK_EX);
    if($ret === false) {
        die('There was an error writing ip file');
    }   
    else {
        echo "Save your IP<br><br>";
        echo "Configuration is done. Enjoy! :)<br>";
    }   
}   
else {
   die('no post data to process');
} 
