<?php
if (isset($_GET['user']) and isset($_GET['msg']) and isset($_GET['chat'])) {
	sendmsg($_GET['user'],$_GET['msg'],$_GET['chat']);
}
else {
	echo "erreur dans les attributs";
}
function sendmsg($user,$msg,$chat) {
	$content = $user." : ".$msg;
	$file = fopen("chats/".$chat."/chatlog.txt","a+");
	fwrite($file,"\n".$content);
	fclose($file);
}
?>