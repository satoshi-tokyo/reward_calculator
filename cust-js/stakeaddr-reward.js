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
                var stage_calc_data = document.getElementById("stage_calc_data");

                if (response.length == 0) {
                    tag_reward_list = '<hr style="border-top-style:dotted;border-top-width:3px;border-top-color:#999;display:inline-block;width:90%"></hr>';
                    tag_reward_list += '<figure class="wp-block-table"><table><tbody><tr>';
                    tag_reward_list += '<tr><th>Epoch</th>';
                    tag_reward_list += '<th>Reward (ADA)</th>';
                    tag_reward_list += '</tr>';
                    tag_reward_list += '<tr><td>N/A</td>';
                    tag_reward_list += '<td>N/A</td>';
                    tag_reward_list += '</tr>';
                } else {
                    var data = JSON.parse(response);
                    var rwdall = 0
                    var rwdsgr = 0
                    var pool_id = "pool1tjr4zpndkvwkw3du3fvt59f5men6jhuevt7rpx6xw0wcct5kl04"
                    tag_reward_list = '<figure class="wp-block-table"><table><tbody><tr>';
                    tag_reward_list += '<tr><th>Epoch</th>';
                    tag_reward_list += '<th>Reward (ADA)</th>';
                    tag_reward_list += '</tr>';

                    for (var i = data.length - 1; i >= 0; i--) {
                        if (data[i].pool_id == pool_id){
                            rwdsgr += parseInt(data[i].amount, 10);
                        };
                        rwdall += parseInt(data[i].amount, 10);

                        tag_reward_list += '<tr><td>' + data[i].epoch + '</td>';
                        tag_reward_list += '<td>' + data[i].amount / 1000000 + '</td>';
                        tag_reward_list += '</tr>';
                    };
                    tag_calc_data = '<hr style="border-top-style:dotted;border-top-width:3px;border-top-color:#999;display:inline-block;width:90%"></hr>'
                    tag_calc_data += '<font size="2"><figure class="wp-block-table"><table><tbody>';
                    tag_calc_data += '<tr><td>報酬合計(ADA)</td><td>' + rwdall / 1000000 + '</td></tr>';
                    tag_calc_data += '<tr><td>Epochごとの平均報酬(ADA)</td><td>' + rwdall / data.length  / 1000000 + '</td></tr>';
                    tag_calc_data += '<tr><td>SUGARステークプールで得た報酬合計(ADA)</td><td>' + rwdsgr  / 1000000 + '</td></tr>';
                    tag_calc_data += '</tbody></table></font>';
                    stage_calc_data.innerHTML = tag_calc_data;
                    };

                tag_stage_reward_history = '<font size="2">';
                tag_stage_reward_history += tag_reward_list;
                tag_stage_reward_history += "</tbody></table></font>";
                stage_reward_history.innerHTML = tag_stage_reward_history;

            })
            .fail(function (content) {
                content = "Data Not Found."
            });
    });
};