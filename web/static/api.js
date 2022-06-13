var update_button = document.getElementById("update-button");
update_button.addEventListener("click", function() {
    let dates_form = document.getElementById("dates-form");
    start_date = dates_form.elements["start-date"].value;
    end_date = dates_form.elements["end-date"].value;
    let teams = [];
    let teams_form = document.getElementById("teams-form");
    for (let i = 0; i < teams_form.children.length; i++) {
        if (teams_form.children[i].children[0].checked) {
            teams.push(teams_form.children[i].children[0].id);
        }
    }
    let attrs = [];
    let attrs_form = document.getElementById("attrs-form");
    for (let i = 0; i < attrs_form.children.length; i++) {
        if (attrs_form.children[i].children[0].checked) {
            attrs.push(attrs_form.children[i].children[0].id);
        }
    }
    console.log(start_date, end_date);
    console.log(teams);
    console.log(attrs);
    $.ajax({
        url: "/api",
        type: "POST",
        datatype: "json",
        data: {
            "start_date": start_date,
            "end_date": end_date,
            "teams": teams,
            "attrs": attrs,
        },
        success: function(data) {
            console.log(data);
        }
})});