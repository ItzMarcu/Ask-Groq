import {fetchData} from "./response";

const userInput = document.getElementById("userInput");
const botMessages = document.getElementById("botResponse");
const userMessages = document.getElementById("userInput");
const submitBtn = document.getElementById("submit");

submitBtn.addEventListener("click", () => {
    if (userInput && userMessages) {
        text = userInput.value.trim();
        if (!text) return;

        addUserMessage(text);

        response = fetchData(text);
        
        addResponseMessage(text);
    }

    console.error("Error: HTML document changed");
    //addResponseMessage() // passare 
    return;
});

function addResponseMessage(text) {
    if (!text) {
        console.error("Error: response text value is null");
        return;
    }

    if (!botMessages) {
        console.error("Error: botResponse div not found");
        return;
    }

    botMessages.innerText = text;
    return;
}

function addUserMessage(text) {
    if (!text) {
        console.error("Error: user text value is null");
        return;
    }

    if (!userInput) {
        console.error("Error: userInput field not found");
        return;
    }

    userInput.innerText = text;
    return;
}