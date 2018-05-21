<?php 
	include "check.php";
	if (!check()) {
		header('Location: '.'..?p=n');
	}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Larvalord</title>
	<script src="../data/jslibraries/jquery.js"></script>
</head>
<body>
	<?php 
		include "../background.php";
		include "profile.php";
		include "chatbox.php";
	?>
</body>
</html>