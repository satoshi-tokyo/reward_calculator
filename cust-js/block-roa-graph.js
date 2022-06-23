var pool_id;
var pool_id_bech32;
var blocks_epoch;
var blocks_lifetime;
var roa;
var roa_lifetime;
var luck_lifetime;
var hist_roa = [];
var chartVal_hist_roa = [];
var chartVal_hist_bpe = [];
getData();

function getData() {
    const url = 'https://js.adapools.org/pools/5c8751066db31d6745bc8a58ba1534de67a95f9962fc309b4673dd8c/summary.json';
    $.getJSON(url, (data) => {
        pool_id = data.data.pool_id;
        pool_id_bech32 = data.data.pool_id_bech32;
        blocks_epoch = data.data.blocks_epoch;
        blocks_lifetime = data.data.blocks_lifetime;
        roa = data.data.roa;
        roa_lifetime = data.data.roa_lifetime;
        luck_lifetime = data.data.luck_lifetime;
        active_stake = data.data.active_stake;
        total_stake = data.data.total_stake;
        saturated = data.data.saturated;

        // Parameters (Historical ROA%)
        hist_roa = JSON.parse(data.data.hist_roa);
        chartVal_hist_roa.push(['Epoch', 'ROA(%)', { role: "style" }, { role: 'annotation' }]);
        for (let i = 0; i < hist_roa.length; i++) {
            p1 = [hist_roa[i].e.toString(), parseFloat(hist_roa[i].val), '#77add1', parseFloat(hist_roa[i].val)];
            chartVal_hist_roa.push(p1);
        };

        // Parameters (Historical Blocks)
        hist_bpe = JSON.parse(data.data.hist_bpe);
        chartVal_hist_bpe.push(['Epoch', 'Blocks', { role: "style" }, { role: 'annotation' }]);
        for (let i = 0; i < hist_bpe.length; i++) {
            p2 = [hist_bpe[i].e.toString(), parseInt(hist_bpe[i].val), '#77add1', parseInt(hist_bpe[i].val)];
            chartVal_hist_bpe.push(p2);
        };

        // Parameters
        poolId = 'Pool id: ' + pool_id;
        poolIdDaedalus = 'Pool id (Daedalus): ' + pool_id_bech32;
        epochBlock = 'Epoch Block: ' + blocks_epoch;
        lifeTimeBlock = 'Lifetime Block: ' + blocks_lifetime;
        ROAMonth = 'ROA (M): ' + roa + '%';
        ROALifeTime = 'ROA Lifetime: ' + roa_lifetime + '%';
        luckLifeTime = 'Luck Lifetime: ' + luck_lifetime + '%';
        ActiveStake = 'Active Stake: ' + active_stake;
        TotalStake = 'Total Stake: ' + total_stake;
        Saturated = 'Saturation: ' + Math.round(saturated * 100) + '%';

        // Render
        var stage_block = document.getElementById('stage_block');
        var stage_roa = document.getElementById('stage_roa');
        tag = "<font size='2' color='#77add1'>"
        // tag = "<span>" + poolId + "</span><br>";
        // tag += "<span>" + poolIdDaedalus + "</span><br>";
        tag_block = tag + epochBlock + "<br>";
        tag_block += lifeTimeBlock + "<br>";
        tag_block += "</font>";

        tag_roa = tag + ROAMonth + "<br>";
        tag_roa += ROALifeTime + "<br>";
        tag_roa += luckLifeTime + "<br>";
        tag_roa += "</font>";
        // tag += "<span>" + ActiveStake + "</span><br>";
        // tag += "<span>" + TotalStake + "</span><br>";
        // tag += "<span>" + Saturated + "</span><br>";
        stage_block.innerHTML = tag_block;
        stage_roa.innerHTML = tag_roa;

        // Draw chart of Historical ROA(%)
        google.charts.load('current', { packages: ['corechart'] });
        google.charts.setOnLoadCallback(drawChart1);
        google.charts.setOnLoadCallback(drawChart2);
    });
};

function drawChart1() {
    var data = google.visualization.arrayToDataTable(chartVal_hist_bpe);
    var options = {
        'title': 'Blocks per Epoch',
        'titleTextStyle':
        {
            'color': '#77add1',
            'bold': false,
            'fontSize': 16
        },
        'legend': {
            'position': 'none',
        },
        'annotations': {
            'alwaysOutside': true,
            'datum': {
                'stem': {
                    'length': 0
                }
            }
        },
        'animation': {
            'startup': true,
            'easing': 'linear',
            'duration': 1000
        },
        'hAxis': {
            'title': 'Epoch',
            'titleTextStyle': {
                'color': '#77add1',
                'italic': false
            },
            'textStyle': { 'color': '#77add1' },
            'gridlines': {
                'count': 0
            }
        },
        'vAxis': {
            'title': 'Blocks',
            'titleTextStyle': {
                'color': '#77add1',
                'italic': false
            },
            'textStyle': { 'color': '#77add1' },
            'baselineColor': '#77add1',
            'gridlines': {
                'count': 0
            }
        },
        'width': 350,
        'height': 300
    };
    var stage = document.getElementById('stage1');
    var chart = new google.visualization.LineChart(stage);
    chart.draw(data, options);
};

function drawChart2() {
    var data = google.visualization.arrayToDataTable(chartVal_hist_roa);
    var options = {
        'title': 'ROA(%) per Epoch',
        'titleTextStyle':
        {
            'color': '#77add1',
            'bold': false,
            'fontSize': 16
        },
        'legend': {
            'position': 'none',
        },
        'annotations': {
            'alwaysOutside': true,
            'datum': {
                'stem': {
                    'length': 0
                }
            }
        },
        'animation': {
            'startup': true,
            'easing': 'linear',
            'duration': 1000
        },
        'hAxis': {
            'title': 'Epoch',
            'titleTextStyle': {
                'color': '#77add1',
                'italic': false
            },
            'textStyle': { 'color': '#77add1' },
            'gridlines': {
                'count': 0
            }
        },
        'vAxis': {
            'title': 'ROA(%)',
            'titleTextStyle': {
                'color': '#77add1',
                'italic': false
            },
            'textStyle': { 'color': '#77add1' },
            'baselineColor': '#77add1',
            'gridlines': {
                'count': 0
            }
        },
        'width': 350,
        'height': 300
    };
    var stage = document.getElementById('stage2');
    var chart = new google.visualization.ColumnChart(stage);
    chart.draw(data, options);
};
