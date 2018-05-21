<?php
session_start();
function check() {
	$root = $_SERVER['DOCUMENT_ROOT'].'/';
	$pseudo;
	$password;
	$chat;
	if (isset($_POST['pseudo']) and isset($_POST['password'])) {
		$pseudo = $_POST['pseudo'];
		$password = $_POST['password'];
	}
	else if (isset($_SESSION['pseudo']) and isset($_SESSION['password'])){
		$pseudo = $_SESSION['pseudo'];
		$password = $_SESSION['password'];
	}
	else {
		return false;
	}
	if (!isset($_SESSION['chat'])) {
		$_SESSION['chat'] = "mainchat";
	}
	if (is_dir($root.'users/'.$pseudo)) {
		$file = fopen($root.'users/'.$pseudo.'/password.txt','r');
		$content = fgets($file);
		if ($content == $password) {
			$_SESSION['pseudo'] = $pseudo;
			$_SESSION['password'] = $password;
			return true;
		}
		else {
			return false;
		}
		fclose($file);
	}
	else {
		return false;
	}
}
?>