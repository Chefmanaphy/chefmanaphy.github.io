<?php
function rrmdir($dir) {
   if (is_dir($dir)) {
     $objects = scandir($dir);
     foreach ($objects as $object) {
       if ($object != "." && $object != "..") {
         if (filetype($dir."/".$object) == "dir") rrmdir($dir."/".$object); else unlink($dir."/".$object);
       }
     }
     reset($objects);
     rmdir($dir);
   }
} 
$user = $_GET['user'];
$dir = 'users/'.$user;
if (is_dir($dir)) {
	rrmdir($dir);
	echo $user." a été supprimé";
}
else {
	echo $user." n'est pas attribué";
}