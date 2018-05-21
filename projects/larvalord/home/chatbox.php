<div id="chatbox" class="chatbox">
	<div class="messages" id="messages"></div>
	<div class="chatlist" id="chatlist">
		<div id="liist"></div>
		<p class="result" id="result">mainchat</p>
	</div>
	<center>
		<form action="javascript:clearthat()" class="sending">
			<input type="text" id="in"/>
			<input type="submit"></input>
		</form>
	</center>
</div>
<script>
	function clearthat() {
		var xhr = new XMLHttpRequest;
		xhr.open("GET","sendmsg.php?user=<?php echo $_SESSION['pseudo'];?>&msg="+document.getElementById("in").value+"&chat="+document.getElementById("result").innerHTML);
		xhr.send();
		document.getElementById("in").value="";	
	}
	function refreshchat() {
		var element = document.getElementById("messages")
		var oldcontent = element.innerHTML;
		var xhr = new XMLHttpRequest;
		xhr.onreadystatechange = function() {
			if (this.readyState==4 && this.status == 200) {
				element.innerHTML = this.responseText;
				if (oldcontent != element.innerHTML) {
					element.scrollTop = element.scrollHeight - element.clientHeight;
				}
			}
		}
		var result = document.getElementById("result");
		xhr.open("GET","getmsgs.php?chat="+result.innerHTML);
		xhr.send();
	}
	setInterval(refreshchat,100);
	refreshchat();
	function getchats() {
		var xhr = new XMLHttpRequest;
		xhr.onreadystatechange = function() {
			if (this.readyState==4 && this.status==200) {
				document.getElementById("liist").innerHTML = this.responseText;
				var elements = document.getElementsByClassName("elmt");
				for (var i=0;i<elements.length;i++) {
					elements[i].onclick = function() {
						document.getElementsByClassName("result")[0].innerHTML = this.innerHTML;
					}
				}
			}
		}
		xhr.open("GET","chatrooms.php");
		xhr.send();
	}
	getchats();
</script>
<style>
	.chatbox {
		width:25vw;
		overflow:hidden;
		background:#fff;
		margin-left:20px;
		margin-top:20px;
		border-radius:20px;
		height:80vh;
		float:right;
	}
	.messages {
		overflow:auto;
		height:70vh;
		width:60%;
		float:left;
		margin-left:5%;
		margin-top:5%;
		border:3px solid #777;
	}
	.sending {
		margin-top:5vh;
	}
	.sending input {
		border:2px solid red;
	}
	.chatbox * {
	}
	.chatlist {
		border:3px solid #777;
		width:20%;
		overflow:hidden;
		float:right;
		margin-right:5%;
		margin-top:5%;
	}
	.elmt:hover {
		background:#555;
	}
</style>