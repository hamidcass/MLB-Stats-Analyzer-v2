const category_chooser_cont = document.getElementById("category_chooser");
const offensive_button = document.getElementById("offensive_button");
const pitching_button = document.getElementById("pitching_button");

//get choice of button
offensive_button.addEventListener("click", function () {
  //get choice
  send_category("Offense");
});
pitching_button.addEventListener("click", function () {
  //get choice
  send_category("Pitching");
});

function send_category(choice) {
  fetch("/views/collect_category", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ category: choice }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      return response.text(); // Assuming the server returns HTML content as a string
    })
    .then((html) => {
      // Replace the content of an element with ID 'container' with the received HTML
      document.body.innerHTML = html;
      get_stats(choice);
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}

//send offensive stats to views.py
function send_o_stats(stat_1, stat_2, choice) {
  const stats_chooser_cont = document.getElementById("stats_chooser");
  fetch("/views/collect_offensive_stats", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ first_stat: stat_1, second_stat: stat_2 }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      return response.text(); // Assuming the server returns HTML content as a string
    })
    .then((html) => {
      // Replace the content of an element with ID 'container' with the received HTML
      document.body.innerHTML = html;
      process_results(stat_1, stat_2, choice);
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}

//send pitching stats to views.py
function send_p_stats(stat_1, stat_2, choice) {
  const stats_chooser_cont = document.getElementById("stats_chooser");
  fetch("/views/collect_pitching_stats", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ first_stat: stat_1, second_stat: stat_2 }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok.");
      }
      return response.text(); // Assuming the server returns HTML content as a string
    })
    .then((html) => {
      // Replace the content of an element with ID 'container' with the received HTML
      document.body.innerHTML = html;
      process_results(stat_1, stat_2, choice);
    })
    .catch((error) => {
      console.error("There was an error:", error);
    });
}

function get_stats(choice) {
  const choose_stat_button_1 = document.getElementById("stat_1");
  const choose_stat_button_2 = document.getElementById("stat_2");
  const submit_button = document.getElementById("submit_button");
  const dropdown_container_2 = document.getElementById("dropdown_container_2");
  const ddOptions = document.getElementsByClassName("dd_option");

  stat_category = choice;
  let chosen_stat;
  let stat_1_selected = false;
  let stat_2_selected = false;

  choose_stat_button_1.addEventListener("mouseover", function () {
    dropdown_container_2.style.visibility = "visible";
    choose_stat_button_1.style.fontSize = "25px";
    chosen_stat = choose_stat_button_1;
  });
  choose_stat_button_1.addEventListener("mouseout", function () {
    dropdown_container_2.style.visibility = "hidden";
    choose_stat_button_1.style.fontSize = "20px";
  });

  choose_stat_button_2.addEventListener("mouseover", function () {
    dropdown_container_2.style.visibility = "visible";
    choose_stat_button_2.style.fontSize = "25px";
    chosen_stat = choose_stat_button_2;
  });
  choose_stat_button_2.addEventListener("mouseout", function () {
    dropdown_container_2.style.visibility = "hidden";
    choose_stat_button_2.style.fontSize = "20px";
  });

  dropdown_container_2.addEventListener("mouseover", function () {
    dropdown_container_2.style.visibility = "visible";
    chosen_stat.style.fontSize = "25px";
  });

  dropdown_container_2.addEventListener("mouseout", function () {
    dropdown_container_2.style.visibility = "hidden";
    chosen_stat.style.fontSize = "20px";
  });

  //this will always change the stat 1 button. Maybe nest it inside the event listener
  //to make it change whichever button is pressed?

  Array.from(ddOptions).forEach((option) => {
    option.addEventListener("click", function (event) {
      chosen_stat.innerHTML = event.target.textContent;
      if (chosen_stat == choose_stat_button_1) {
        stat_1_selected = true;
      } else if (chosen_stat == choose_stat_button_2) {
        stat_2_selected = true;
      }

      if (stat_1_selected == true && stat_2_selected == true) {
        //both stats have been selected
        //make submit button active
        submit_button.style.backgroundColor = "#2828ff";
        submit_button.addEventListener("click", function () {
          if (choice == "Offense") {
            send_o_stats(
              choose_stat_button_1.textContent,
              choose_stat_button_2.textContent,
              choice
            );
          } else {
            send_p_stats(
              choose_stat_button_1.textContent,
              choose_stat_button_2.textContent,
              choice
            );
          }
        });
      }
    });
  });
}

function process_results(stat_1, stat_2, choice) {
  var graph = document.getElementById("graph_data").textContent;
  var parsedGraphData = JSON.parse(graph);

  const search_bar = document.getElementById("input_player");
  const search_button = document.getElementById("search_player_button");

  document.getElementById("graph_data").remove();
  graph_container = document.getElementById("g_container");
  var layout = {
    autosize: false,
    width: 500,
    height: 500,
    margin: {
      l: 50,
      r: 50,
      b: 100,
      t: 100,
      pad: 4,
    },
  };

  //config doesn't work (cannot scroll with mouse wheel)
  var config = {
    scrollZoom: true, // Enable scroll zoom
  };

  Plotly.plot(graph_container, parsedGraphData, layout, config);

  //user can search for a player
  search_button.addEventListener("click", function () {
    if (search_bar.value.trim() !== "") {
      fetch("/views/search_player", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          first_stat: stat_1,
          second_stat: stat_2,
          category: choice,
          player: search_bar.value.trim(),
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok.");
          }
          return response.text(); // Assuming the server returns HTML content as a string
        })
        .then((html) => {
          // Replace the content of an element with ID 'container' with the received HTML
          document.body.innerHTML = html;
          process_results(stat_1, stat_2, choice);
        })
        .catch((error) => {
          console.error("There was an error:", error);
        });
    }
  });
}
