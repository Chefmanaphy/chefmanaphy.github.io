<?php
	if (isset($_GET['chat'])) {
		$a = $_GET['chat'];
	}
	else {
		$a = "mainchat";
	}
	if (is_file("chats/".$a."/chatlog.txt")) {
		$chat = fopen("chats/".$a."/chatlog.txt",'r');
		$lines = [];
		echo "<ul>";
		while (!feof($chat)) {
			$line = fgets($chat);
			if ($line != "") {
				array_push($lines,$line);
			}
		}
		for ($i=0;$i<count($lines);$i++) {
			if ($i != 0) {
				echo "<li>".$lines[$i]."</li>";
			}
		}
		echo "</ul>";
	}
	else {
		echo "chat non existant";
	}
?>