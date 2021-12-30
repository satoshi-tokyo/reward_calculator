getEpoch();

function getEpoch() {
    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/data.json';
    $.getJSON(url, (data) => {
        var epoch;
        var current_epoch;
        epoch = data.epoch;
        current_epoch = epoch + 2;

        // Render
        var stage_current_epoch = document.getElementById('stage_current_epoch');
        tag = "<font size='2' color='#1e90f'>";
        tag_epoch = tag + "Current Epoch (現在のエポック): <b>" + current_epoch + "</b><br></font>";
        stage_current_epoch.innerHTML = tag_epoch;
    });
};


function clickBtnOptReward() {
    var textbox = document.getElementById("input_test_stake");
    var inputValue = textbox.value;
    getGeneralReward(inputValue);
};

function getGeneralReward(inputValue) {
    var epoch;
    var current_epoch;
    var f_s_sigma;
    var pool_fee;
    var delegators_reward;
    var pool_active_stake;

    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/data.json';
    $.getJSON(url, (data) => {
        epoch = data.epoch;
        current_epoch = epoch + 2;
        f_s_sigma = data.f_s_sigma;
        pool_fee = data.pool_fee;
        delegators_reward = f_s_sigma - pool_fee;
        pool_active_stake = data.pool_active_stake;

        delegator_stake_in_ada = inputValue;
        delegator_stake = inputValue * 1000000;
        calculated_reward_in_ada = delegators_reward * delegator_stake / pool_active_stake / 1000000;
        calculated_reward_in_ada_rounded = Math.round(calculated_reward_in_ada * 100) / 100;

        console.log(calculated_reward_in_ada);
        console.log(calculated_reward_in_ada_rounded);
        console.log(delegator_stake);

        ros = (((calculated_reward_in_ada / delegator_stake_in_ada) + 1) ** 73) - 1;
        monthly_calculated_reward_in_ada = delegator_stake_in_ada * ros / 73 * 6
        monthly_calculated_reward_in_ada_rounded = Math.round(monthly_calculated_reward_in_ada * 100) / 100;

        annual_calculated_reward_in_ada = delegator_stake_in_ada * ros
        annual_calculated_reward_in_ada_rounded = Math.round(annual_calculated_reward_in_ada * 100) / 100;
        console.log(ros)

        // Render
        var stage_test_reward = document.getElementById('stage_test_reward');

        tag = "<font size='2' color='#1e90f'>";
        tag_test_reward = tag + "Epoch (エポック): ";
        tag_test_reward += tag + "<b>" + calculated_reward_in_ada_rounded + "</b> ADA<br>";
        tag_test_reward += tag + "Monthly (月間): <b>" + monthly_calculated_reward_in_ada_rounded + "</b> ADA<br>";
        tag_test_reward += tag + "Annual (年間): <b>" + annual_calculated_reward_in_ada_rounded + "</b> ADA<br>";
        tag_test_reward += "</font>";

        stage_test_reward.innerHTML = tag_test_reward;
    });
};
