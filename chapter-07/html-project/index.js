const btn = document.getElementById("btnClickMe");
const textDisplay = document.getElementById("textDisplay");
let clickCount = 0;

btn.onclick = function() {
    clickCount++;
    textDisplay.textContent = String(clickCount);
}