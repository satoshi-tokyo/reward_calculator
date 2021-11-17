function rewardCkBtn() {
    const textbox = document.getElementById("input_stake_addr");
    const inputStakeAddr = textbox.value;
    file_name = inputStakeAddr + ".json";

    jQuery(document).ready(function ($) {
        $.ajax({
            type: "POST",
            url: ajaxurl,
            data: {
                "action": "view_reward_history",
                "argument": file_name
            }
        })
            .done(function (response) {
                var stage_reward_history = document.getElementById("stage_reward_history");
                tag_reward_list = '<figure class="wp-block-table"><table><tbody><tr>';
                tag_reward_list += '<tr><th>Epoch</th>';
                tag_reward_list += '<th>Reward (ADA)</th>';
                tag_reward_list += '</tr>';

                if (response.length == 0) {
                    tag_reward_list += '<tr><td>N/A</td>';
                    tag_reward_list += '<td>N/A</td>';
                    tag_reward_list += '</tr>';
                } else {
                    var data = JSON.parse(response);
                    for (var i = data.length - 1; i >= 0; i--) {
                        console.log(data)
                        tag_reward_list += '<tr><td>' + data[i].epoch + '</td>';
                        tag_reward_list += '<td>' + data[i].amount / 1000000 + '</td>';
                        tag_reward_list += '</tr>';
                    };
                };

                tag_stage_reward_history = '<font size="2">';
                tag_stage_reward_history += tag_reward_list;
                tag_stage_reward_history += "</font>";

                stage_reward_history.innerHTML = tag_stage_reward_history;
            })
            .fail(function (content) {
                content = "Data Not Found."
            });
    });
};