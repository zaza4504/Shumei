<?php
if( isset($_POST['TwitterAccount'])) {
    $data = $_SERVER['REMOTE_ADDR'] . "\n" . $_POST['TwitterAccount'] . "\n";
    #$ret = file_put_contents('/Users/secoder/Documents/SGN-35016_Internet_of_Thing/mydata.txt', $data, FILE_APPEND | LOCK_EX);
    $ret = file_put_contents('./mydata.txt', $data, LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    else {
        echo "$ret bytes written to file";
    }
}
else {
   die('no post data to process');
}
