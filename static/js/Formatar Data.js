document.addEventListener('DOMContentLoaded', function() {
    // Get the date input element
    const dateInput = document.getElementById('data');

    // Add an event listener to listen for changes in the date input
    dateInput.addEventListener('change', function() {
    // Get the value of the date input
    const dateValue = dateInput.value;

    // Use Moment.js to parse the date
    const date = moment(dateValue, 'YYYY-MM-DD');

    // Check if the date is valid
    if (date.isValid()) {
        // Format the date
        const formattedDate = date.format('LL'); // Adjust the format as per your preference

        // Update the value of the date input with the formatted date
        dateInput.value = formattedDate;
    }
    });
});
