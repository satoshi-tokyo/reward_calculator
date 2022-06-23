var ada_price_usd;
var ada_price_jpy;

getAdaPrice();

function getAdaPrice() {
    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/ada_price/main/data/data.json';
    $.getJSON(url, (data) => {
        ada_price_usd = data.cardano.usd;
        ada_price_jpy = data.cardano.jpy;

        // Render
        var stage_ada_price = document.getElementById('stage_ada_price');
        tag = "<font size='3' color='#1e90ff'>";
        tag_ada_price = tag + "<b>" + ada_price_usd + " USD</b><br>";
        tag_ada_price += "<b>" + ada_price_jpy + " JPY</b><br></font>";
        stage_ada_price.innerHTML = tag_ada_price;
    });
};