getTimings();

function getTimings() {
    const url = 'https://raw.githubusercontent.com/satoshi-tokyo/reward_calculator/main/json/epoch_stake_timing.json';
    $.getJSON(url, (data2) => {
        console.log(data2)
        tag_timing = '<figure class="wp-block-table"><table><tbody><tr>'
        tag_timing += '<tr><th>Epoch</th>'
        tag_timing += '<th>Epoch Start</th>'
        tag_timing += '<th>Epoch End</th>'
        tag_timing += '<th>Deleg Epoch</th>'
        tag_timing += '<th>Deleg Epoch Start</th>'
        tag_timing += '<th>Deleg Epoch End</th>'
        tag_timing += '</tr>'
        for (let i = 0; i < data2.length; i++) {
            if (i == 4) {
                tag_timing += '<tr><td><b>' + data2[i].epoch + '</b></td>'
                tag_timing += '<td><b>' + data2[i].start_time + '</b></td>'
                tag_timing += '<td><b>' + data2[i].end_time + '</b></td>'
                tag_timing += '<td><b>' + data2[i].epoch_deleg + '</b></td>'
                tag_timing += '<td><b>' + data2[i].start_time_deleg + '</b></td>'
                tag_timing += '<td><b>' + data2[i].end_time_deleg + '</b></td>'
                tag_timing += '</tr>'

            } else {
                tag_timing += '<tr><td>' + data2[i].epoch + '</td>'
                tag_timing += '<td>' + data2[i].start_time + '</td>'
                tag_timing += '<td>' + data2[i].end_time + '</td>'
                tag_timing += '<td>' + data2[i].epoch_deleg + '</td>'
                tag_timing += '<td>' + data2[i].start_time_deleg + '</td>'
                tag_timing += '<td>' + data2[i].end_time_deleg + '</td>'
                tag_timing += '</tr>'
            };
        };
        tag_timing += '</tbody></table></figure>'
        stage_timing.innerHTML = tag_timing;
    });
};
