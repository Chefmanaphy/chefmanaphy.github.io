<?php 
	if (isset($_GET['chat'])) {
		ftruncate(fopen("chats/".$_GET['chat']."/chatlog.txt",'r+'),0);
		echo "chatlog effacé";
	}
	else {
		echo "erreur dans les attributs";
	}
?>