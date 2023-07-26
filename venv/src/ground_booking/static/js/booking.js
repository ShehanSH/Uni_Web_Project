var btn = document.querySelectorAll("form .btn")[0];

var checkBox = document.getElementById("exampleCheck1");
btn.disabled = !checkBox.checked;

checkBox.addEventListener("change",checkTerms);

function checkTerms(){
	if(this.checked){
		btn.disabled = false;
	}else{
		btn.disabled = true;
	}
}



