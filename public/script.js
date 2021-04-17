const currentPassage = document.getElementById("current");
const previousPassage = document.getElementById("previous");

async function fetchPassage() {
    const response = await fetch("https://drsvfxtdvi.execute-api.us-east-1.amazonaws.com/dev/passage");
    const body = await response.json()

    const current = currentPassage.textContent;
    currentPassage.textContent = body.passage;
    previousPassage.textContent = current;

    restartAnimations(currentPassage, previousPassage);
}

// from: https://stackoverflow.com/a/45036752
function restartAnimations(...elements) {
    elements.forEach(function(element) {
        element.style.animation = 'none';
        element.offsetHeight;
        element.style.animation = null;
    });
}

const screenReaderExplanation = document.getElementById("screenreader-explanation");
screenReaderExplanation.innerHTML = "Below shifting clouds and above swaying waves, forty characters of James’ Joyce’s “Finnegan’s Wake” are displayed, progressing forward every four seconds through the cyclical novel, endlessly. They will be read aloud as they appear.";

fetchPassage();
setInterval(fetchPassage, 4e3);