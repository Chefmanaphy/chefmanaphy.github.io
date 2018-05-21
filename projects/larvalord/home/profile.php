<div class="profile" id="profile">
	<center>
		<p class="pseudo"><?php echo $_SESSION['pseudo'];?></p><br>
	</center>
	<ul class="titres">
		<?php 
			if (is_file('../users/'.$_SESSION['pseudo']."/titres.txt")) {
				$ftitres = fopen('../users/'.$_SESSION['pseudo']."/titres.txt",'r');
				$titres = [];
				while (!feof($ftitres)) {
					array_push($titres,fgets($ftitres));
					
				}
				foreach ($titres as $titre) {
					echo "<li>".$titre."</li>";
				}
			}
			else {
				echo "Aucun titre, tu es nul.";
			}
		?>
	</ul>
</div>
<style>
	.profile {
		width:25vw;
		overflow:hidden;
		background:#fff;
		margin-left:20px;
		margin-top:20px;
		border-radius:20px;
		height:80vh;
		float:left;
	}
	.profile * {
		margin:0;
	}
	.pseudo {
		font-size:3em;
	}
</style>