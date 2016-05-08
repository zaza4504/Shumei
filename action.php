<?php
if(isset($_POST['MACAddress']) && isset($_POST['TwitterAccount'])) {
    $data = $_SERVER['REMOTE_ADDR'] . "\n" . $_POST['MACAddress'] . "\n" . $_POST['TwitterAccount'] . "\n";
    #$ret = file_put_contents('/home/pi/Projects/IoT/mydata.txt', $data, FILE_APPEND | LOCK_EX);
    $ret = file_put_contents('/home/pi/Projects/IoT/mydata.txt', $data, LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "\nConfiguration is Done. Enjoy! :)";
    }
}
else {
   die('no post data to process');
}
