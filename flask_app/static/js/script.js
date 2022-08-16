const indexForms = document.getElementById('LogAndReg');

let showFormBtn = document.getElementById('toggle');



showFormBtn.onclick = function showForms(){
    if(indexForms.className !== "LogAndReg"){
        indexForms.className = "LogAndReg";
    }
    else{
        indexForms.className = 'LogAndRegAnimate';
    }
}
