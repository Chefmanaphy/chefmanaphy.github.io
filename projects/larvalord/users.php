<script>
	function remove(user) {
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
			if (xhr.readyState == 4) {
				location.reload();
			}
		};
		xhr.open("GET","removeuser.php?user="+user);
		xhr.send();
	}
</script>
<?php
reload();
function reload() {
	$users = scandir("users");
	foreach ($users as $user) {
		if ($user != "." and $user != ".."){
			echo "<button onclick=\"remove('".$user."')\">X</button>".$user."<br>";
		}
	}
}
?>

<form method="post" action="register.php" target="_blank">
	<input type="text" name="username">
	<input type="password" name="password">
	<input type="email" name="email">
	<input type="submit">
</form>