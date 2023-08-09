document.addEventListener('DOMContentLoaded', function() {
  // Get the time input element
  const timeInput = document.getElementById('horario');

  // Add an event listener to listen for changes in the time input
  timeInput.addEventListener('change', function() {
    // Get the value of the time input
    const timeValue = timeInput.value;

    // Use Moment.js to parse the time
    const time = moment(timeValue, 'HH:mm');

    // Check if the time is valid
    if (time.isValid()) {
      // Format the time
      const formattedTime = time.format('LT'); // Adjust the format as per your preference

      // Update the value of the time input with the formatted time
      timeInput.value = formattedTime;
    }
  });
});