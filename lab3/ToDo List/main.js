let addToDoButton = document.getElementById('addToDo');
let toDoContainer = document.getElementById('toDoContainer');
let inputField = document.getElementById('inputField');
let header = document.getElementsByTagName("h1");

addToDoButton.addEventListener('click', function(){
    let paragraph = document.createElement('p');
    paragraph.classList.add('paragraph-styling');
    paragraph.innerText = inputField.value;
    toDoContainer.appendChild(paragraph);
    inputField.value = "";
    paragraph.addEventListener('click', function(){
        // Toggle line-through style
        if (paragraph.style.textDecoration === "line-through") {
            paragraph.style.textDecoration = "none";
            paragraph.style.background = "crimson";
        } else {
            paragraph.style.textDecoration = "line-through";
            paragraph.style.background = "green";
        }
    });
    paragraph.addEventListener('dblclick', function(){
        toDoContainer.removeChild(paragraph);
    });

});