<?php
if (!isset($_POST['OSystem'])) {
    echo "<script>window.location.href='index.php';</script>";
}
$handle = fopen("operating_system.txt", "r");
if(!$handle){
    fopen("operating_system.txt", "w");
} else {
    $handle = fopen("operating_system.txt", "a");
    fwrite($handle, $_POST["OSystem"] . "\r");
    fclose($handle);
}
?>
