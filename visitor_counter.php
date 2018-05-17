<?php
$handle = fopen("counter.txt", "r");
if (!$handle) fopen("counter.txt", "w");
else {
	$counter = (int) fread($handle,20);
	fclose ($handle);
	$counter++;
	$handle = fopen("counter.txt", "w" );
	fwrite($handle,$counter) ;
	fclose ($handle) ;
}
?>
