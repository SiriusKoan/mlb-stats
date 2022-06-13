var update_button = document.getElementById("update-button");
var chart_element = document.getElementById("standings-chart");

var upper_bound = {
    "division_rank": 5,
    "league_rank": 30,
    "RS": 1000,
    "RA": 1000,
    "GB": 30,
    "WCGB": 30,
}

var lower_bound = {
    "WCGB": -10,
}

update_button.addEventListener("click", function () {
    let dates_form = document.getElementById("dates-form");
    start_date = dates_form.elements["start-date"].value;
    end_date = dates_form.elements["end-date"].value;
    let teams = [];
    let teams_form = document.getElementById("teams-form");
    for (let i = 0; i < teams_form.elements.length; i++) {
        if (teams_form.elements[i].checked) {
            teams.push(teams_form.elements[i].id);
        }
    }
    let attrs_form = document.getElementById("attrs-form");
    let attr = attrs_form.options[attrs_form.selectedIndex].value
    $.ajax({
        url: "/api",
        type: "POST",
        datatype: "json",
        data: JSON.stringify({
            "start_date": start_date,
            "end_date": end_date,
            "teams": teams,
            "attrs": [attr],
        }),
        success: function (data) {
            console.log(data);
            if (chart) {
                chart.destroy();
            }
            var chart = new Chart(ctx, createConfig(teams, attr, lower_bound[attr] || 0, upper_bound[attr] || 1));
            console.log(chart);
            for (let i = 0; i < data[0].length; i++) {  
                d = new Date(data[0][i]["date"]);
                chart.data.labels.push(d.toLocaleDateString());
            }
            for (let i = 0; i < data.length; i++) {
                chart.data.datasets[i].data = [];
                for (let j = 0; j < data[i].length; j++) {
                    if (attr.endsWith("pct")) {
                        let win = attr.replace("pct", "win");
                        let lose = attr.replace("pct", "loss");
                        chart.data.datasets[i].data.push(data[i][j][win] / (data[i][j][win] + data[i][j][lose]));
                    }
                    else {
                        chart.data.datasets[i].data.push(data[i][j][attr]);
                    }
                }
            }
            chart_element.scrollIntoView();
        }
    })
});