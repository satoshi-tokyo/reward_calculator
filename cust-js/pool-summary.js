getSummary();

function getSummary() {
    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/summary.json';
    $.getJSON(url, (data1) => {
        console.log(data1)
        tag_summary = '<figure class="wp-block-table"><table><tbody><tr>'
        tag_summary += '<tr><th>Epoch</th>'
        tag_summary += '<th>Active Stake (M)</th>'
        tag_summary += '<th>Live Stake (M)</th>'
        tag_summary += '<th>Declared Pledge</th>'
        tag_summary += '<th>Live Pledge</th>'
        tag_summary += '<th>Fixed Cost</th>'
        tag_summary += '<th>Margin (%)</th>'
        tag_summary += '<th>Blocks</th>'
        tag_summary += '<th>Performance (%)</th>'
        tag_summary += '</tr>'
        for (let i = 0; i < data1.length; i++) {
            tag_summary += '<tr><td>' + data1[i].epoch + '</td>'
            tag_summary += '<td>' + data1[i].pool_active_stake + '</td>'
            tag_summary += '<td>' + data1[i].pool_live_stake + '</td>'
            tag_summary += '<td>' + data1[i].declared_pledge + '</td>'
            tag_summary += '<td>' + data1[i].live_pledge + '</td>'
            tag_summary += '<td>' + data1[i].fixed_cost + '</td>'
            tag_summary += '<td>' + data1[i].margin_cost + '</td>'
            tag_summary += '<td>' + data1[i].block_minted + '</td>'
            tag_summary += '<td>' + data1[i].pool_perf + '</td>'
            tag_summary += '</tr>'
        };
        tag_summary += '</tbody></table></figure>'
        stage_summary.innerHTML = tag_summary;
    });
};
