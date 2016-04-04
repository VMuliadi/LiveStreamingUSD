<?php
if (!isset($_POST['location'])) {
    echo "<script>window.location.href='index.php';</script>";
}

$handle = fopen("location.txt", "r");
if(!$handle){
    fopen("location.txt", "w");
} else {
    $handle = fopen("location.txt", "a");
    fwrite($handle, $_POST["location"] . "\r");
    fclose($handle);
}
?>
