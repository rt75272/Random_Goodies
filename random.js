// --------------------------------------
// Random coin flip simulation.
//
// Usage:
//     $ node random.js
//
// --------------------------------------
var n = 999999;
var heads_success_rate =  0;
var heads_wins = 0;
var tails_success_rate = 0;
var tails_wins = 0;

for(var i = 0; i < n; i++) {
    var x = Math.floor(Math.random() * 10);
    choice = "";
    if(x < 5) {
        choice = "Heads";
        heads_wins++;
        heads_success_rate = heads_wins / i; 
    }
    else if(x >= 5) {
        choice = "Tails";
        tails_wins++;
        tails_success_rate = tails_wins / i;
    }
    else {
        choice = "Something blew up";
    }
    console.log("\n" + choice + "\nHeads success rate: " + heads_success_rate);
    console.log("Tails success rate: " + tails_success_rate);
}

document.getElementById("heads").innerHTML = heads_success_rate;
document.getElementById("tails").innerHTML = tails_success_rate;
