<div class="login" id="login">
	<ul class="tabs">
		<li><a href="#tab1">Se connecter</a></li>
		<li><a href="#tab2">S'enregistrer</a></li>
	</ul>
	<div class="logincontent" id="logincontent">
		<div id="tab1" class="tab_content">
			<?php 
				include "login.html";
				if (isset($_GET['p'])){
					if ($_GET['p'] == 'n') {
						echo "<span class=\"red\">Mauvais pseudo/mdp</span><br>";
					}
				}
				if (isset($_GET['a'])) {
					echo "<span class=\"green\">".$_GET['a']." a bien été crée</span><br>";
					echo "<script>document.getElementById(\"pseudo\").value=\"".$_GET['a']."\";</script>";
				}
			?>
		</div>
		<div id="tab2" class="tab_content">
			<?php include "signin.html";?>
		</div>
	</div>
</div>

<script>
$(document).ready(function() {
	$(".tab_content").hide();
	$("ul.tabs li:first").addClass("active").show();
	$("ul.tabs li:first").css("background","#fff");
	$(".tab_content:first").show();
});
$("ul.tabs li").click(function() {
	$("ul.tabs").removeClass("active");
	$("ul.tabs li").css("background","#aaa");
	$(this).addClass("active");
	$(this).css("background","#fff");
	$(".tab_content").hide();
	var activeTab = $(this).find("a").attr("href");
	$(activeTab).fadeIn();
});
</script>

<style>
	.login{
		overflow:hidden;
		margin-left:20px;
		margin-top:20px;
		margin-bottom:0;
		padding:0;
		width:20vw;
		height:80%;
	}
	.login ul.tabs {
		list-style: none;
		float:left;
		height:20px;
		margin:0;
		padding:0;
		width:100%
	}
	.login ul.tabs li {
		border-radius:20px;
		margin:0;
		padding:0;
		height:19px;
		line-height:19px;
		background: #aaa;
		position:relative;
		
	}
	.login ul.tabs li:first-child {
		float: left;
	}
	.login ul.tabs li:last-child {
		float: right;
	}
	.login ul.tabs li a {
		text-decoration:none;
		color:#000;
		display:block;
		font-size: 1em;
		padding:0 20px;
		outline:none;
		font-weight:bold;
	}
	.logincontent {
		background-color:white;
		overflow:hidden;
		border-radius:20px;
		height:100%;
		width:100%;
		display:block;
		margin:0;
	}
	.logincontent input {
		width:10vw;
		height:3vh;
		border: 2px solid #000;
		margin-bottom:20px;
	}
	.logincontent .submit {
		margin-top:30px;
		border:2px solid red;
		margin: 10px;
		color:#200;
		font-size:0.8em;
		height:20px;
	}
	.logincontent * {
		margin:0;
		font-weight:bold;
	}
	span {
		font-weight:bold;
	}
	.red {
		color:red;
	}
	.green {
		color:green;
	}
	
</style>