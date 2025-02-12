const API_URL = " https://randomuser.me/api"

async function getData() {
    try {
        const response = await fetch(API_URL);
        const { results } = await response.json();
        if (!results) { return console.error("No results found") };
        console.log(results);
    }
    catch (error) {
        console.error("Failed to fecth:", error);
    }
}

//getData();

function checkEmpty(s) {
    if (!s || s.trim().length === 0) {
        console.log("Is Empty");
        return;
    }
    console.log("Not Empty:", s);

}

checkEmpty();
checkEmpty("");
checkEmpty(" ");
checkEmpty("Hello");



function compare(a, b) {
    console.log(`\na: ${a} ${typeof (a)}\nb: ${b} ${typeof (b)}`);
    if (a === b) {
        console.log("Equal in value and type");
        return;
    }
    if (a == b) {
        console.log("Equal in value but not in type");
        return;
    }

    console.log("Not equal");

}

compare(1, 1);
compare(1, "1");
compare(1, "0");
