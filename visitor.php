<?php

// if you are php user, you will know this
// right? if not, read cookie and session chapter in PHP.
// Buy in amazon.com or ask your teacher or lecturer
session_start();

// read the latest visitor from counter.txt and add one
// the value will used to mark the visitor with session
// why add one? well, integer start with zero
$visitor = (int) fread(fopen("visitor_counter.txt", "r"), 20) + 1;

// assign the session to new user. if new user, the program
// will generate a new session and add one to the counter
// if not, let user to watch without registering a new session
if (!isset($_SESSION["key"]))   {
    $_SESSION["name"] = "livewisuda1";
    $_SESSION["key"] = "livewisuda1 - " . $visitor;
    $handle = fopen("visitor_counter.txt", "r");
    $counter = (int) fread($handle, 20);
    fclose ($handle);
    $counter++;
    $handle = fopen("visitor_counter.txt", "w");
    fwrite($handle,$counter);
    fclose ($handle);
}

?>
