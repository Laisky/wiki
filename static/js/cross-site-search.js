// https://github.com/TarekRaafat/autoComplete.js
// doc: https://tarekraafat.github.io/autoComplete.js/#/

window.addEventListener("load",  () => {
    const autoCompleteJS = new autoComplete({
        placeHolder: "Search...",
        data: {
            src: async (query) => {
                const resp = await fetch("http://ramjet.xego-dev.basebit.me/crawler/search?q=" + query);
                const data = await resp.json();
                return data;
            },
            keys: ["title"]
        },
        resultItem: {
            highlight: true,
        },
        searchEngine: (query, record) => {
            return record;
        },
        resultsList: {
            maxResults: 20,
        },
        resultItem: {
            element: (item, data) => {
                // console.log("item", item);
                // console.log("data", data);
                item.innerHTML = data.value.title + " - "+ data.value.context;
            },
        }

    });

    document.querySelector("#autoComplete").addEventListener("selection", function (event) {
        // console.log(event.detail);
        window.location = event.detail.selection.value.url;
    });
});
