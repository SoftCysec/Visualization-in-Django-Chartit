// This is an example of a custom script that can be added to the Django Plotly Dash app.

// Here we'll add some interactivity to our dash app.
// For example, we'll add a button that updates the chart when clicked.

// First, let's define a function that will be called when the button is clicked.
function update_chart() {
  // Get the values of the x and y axis inputs.
  var x_axis = document.getElementById("x-axis-input").value;
  var y_axis = document.getElementById("y-axis-input").value;

  // Construct the URL for the API endpoint that will return the updated chart data.
  var url = "/api/chart-data?x_axis=" + x_axis + "&y_axis=" + y_axis;

  // Send an AJAX request to the API endpoint and update the chart with the returned data.
  $.ajax({
    url: url,
    type: "GET",
    success: function (data) {
      Plotly.react("chart", data);
    },
  });
}

// Next, let's add an event listener to the button that will call the update_chart function when clicked.
document
  .getElementById("update-chart-button")
  .addEventListener("click", update_chart);
