<?php 
$files = scandir("chats/");
foreach($files as $file) {
	if ($file != "." and $file != ".." and is_dir("chats/".$file)) {
		echo "<p class=\"elmt\">".$file."</p>";
	}
}
?>
<style>
	p {
		margin: 0;
	}
	.result {
		border-top : 2px solid #777;
	}
</style>