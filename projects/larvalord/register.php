<?php
session_start();

$path = "users/";

if (isset($_POST['username']) and isset($_POST['password']) and isset($_POST['email'])) {
	$requsername = $_POST['username']; 
	$reqpassword = $_POST['password']; 
	$reqemail = $_POST['email'];
	if (is_dir($path.$requsername)) {
		echo $requsername." est déjà attribué";
	}
	else {
		mkdir($path.$requsername,0777);
		$psw = fopen($path.$requsername."/password.txt","w");
		$mal = fopen($path.$requsername."/email.txt","w");
		fwrite($psw,$reqpassword);
		fwrite($mal,$reqemail);
		header('Location: '."index.php?a=".$requsername);
	}
}
else {
	echo "erreur dans les attributs";
}

?>