var epoch;
var current_epoch;
getEpoch();

function getEpoch() {
    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/data.json';
    $.getJSON(url, (data) => {
        epoch = data.epoch;
        current_epoch = epoch + 2;

        // Render
        var stage_block_epoch = document.getElementById('stage_block_epoch');
        tag = "<font size='2' color='#77add1'>";
        tag_epoch = tag + "現在のエポック: <b>" + current_epoch + "</b><br></font>";
        stage_block_epoch.innerHTML = tag_epoch;
    });
};


function clickBtn() {
    const textbox = document.getElementById("input_stake");
    const inputValue = textbox.value;
    getData(inputValue);
};

function getData(inputValue) {
    var epoch;
    var current_epoch;
    var delegators_reward;
    var pool_active_stake;

    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/data.json';
    $.getJSON(url, (data) => {
        epoch = data.epoch;
        current_epoch = epoch + 2;
        delegators_reward = data.delegators_reward;
        pool_active_stake = data.pool_active_stake;

        delegator_stake = inputValue * 1000000;
        calculated_reward_in_ada = delegators_reward * delegator_stake / pool_active_stake / 1000000;
        calculated_reward_in_ada_rounded = Math.round(calculated_reward_in_ada * 100) / 100;

        // Render
        var stage_block_reward = document.getElementById('stage_block_reward');

        tag = "<font size='2' color='#77add1'>";
        tag_block = tag + "エポック" + current_epoch + "での報酬は";
        tag_block += tag + "<b>" + calculated_reward_in_ada_rounded + "</b> ADAです。<br>";
        tag_block += "</font>";

        stage_block_reward.innerHTML = tag_block;
    });
};
