

const closeBtn = document.getElementById('close');
const openBtn = document.getElementById('open');
const mainContainer = document.getElementById('containerShow');

function showForms(){
    const indexForms = document.getElementById('LogAndReg');
    if(indexForms.className !== "LogAndReg"){
        indexForms.className = "LogAndReg";
    }
    else{
        indexForms.className = 'LogAndRegAnimate';
    }
}

closeBtn.onclick = function closeNav(){
    mainContainer.classList.remove('show-nav');
}
openBtn.onclick = function openNav(){
    mainContainer.classList.add('show-nav');
}





