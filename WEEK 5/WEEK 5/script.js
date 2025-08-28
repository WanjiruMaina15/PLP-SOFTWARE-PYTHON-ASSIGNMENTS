// Part 1 Variable declarations and conditionals
let age=25;
if (age>18){
    console.log('You can vote');
}
    else{
        console.log('Too young to vote')
}


// (Part 2) At least 2 custom functions
const sayHello=function(){
    console.log('Hello World from function expression');
}
sayHello();
//arrow function most recent and recommended
const welcome=()=>{
    console.log('Wake up from arrow function');
}
welcome();



// (Part 3) At least 2 loop examples 
let fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"];
console.log("Using for...of loop:");
for (let fruit of fruits) {
    console.log(fruit);
}

// Part 3: While Loop Example - Army Recruitment

let heights = [6.0, 5.8, 5.4, 5.6, 5.2]; // heights of applicants in feet
let index = 0;

while (index < heights.length) {
    let height = heights[index];
    
    if (height > 5.5) {
        console.log(`Height: ${height} ft - Eligible for army recruitment`);
    } else {
        console.log(`Height: ${height} ft - Not eligible for army recruitment`);
    }
    
    index++;
}


// (Part 4) At least 3 DOM interactions 


function changeText(){
    let Title=document.getElementById('Title')
    Title.textContent='Welcome to JavaScript';
    Title.style.color='Red';
}

function changeText() {
    // Create a new heading element
    let newHeading = document.createElement('h1');
    newHeading.textContent = "You clicked the button!";
    document.body.appendChild(newHeading); // add it to the page
}

document.addEventListener('DOMContentLoaded', function() {
    let newPara = document.createElement('p');
    newPara.textContent = "This paragraph was added using JavaScript!";
    document.body.appendChild(newPara); // now body exists
});
