color_table = [
    "rgba(255, 99, 132, 0.8)",
    "rgba(54, 162, 235, 0.8)",
    "rgba(255, 206, 86, 0.8)",
    "rgba(75, 192, 192, 0.8)",
    "rgba(153, 102, 255, 0.8)",
    "rgba(255, 159, 64, 0.8)",
    "rgba(54, 162, 235, 0.8)",
]

function createConfig(types, description, min = null, max = null) {
    datasets = []
    for (var i = 0; i < types.length; i++) {
        datasets.push({
            label: types[i],
            data: [],
            backgroundColor: color_table[i % 7],
            borderWidth: 1,
            fill: false,
        })
    }

    const config = {
        type: "line",
        data: {
            labels: [],
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: description
                }
            },
        },
    };
    min = min || 0;
    max = max || 100;
    config.options.scales = {
        y: {
            min: min,
            max: max,
        }
    }
    return config;
}

var ctx = document.getElementById("standings-chart").getContext("2d");
