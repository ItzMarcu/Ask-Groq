
export async function fetchData(parameter) {
    response = await fetch("http://127.0.0.1:8000/$/q/parameter=(parameter)");
    if (!response.ok) {
        console.error("Error: an error occurred while fetching data");
        return;
    }

    text = await response.text();
    if (!text) {
        console.error("Errror: API response is null")
    }

    return text;
}