document.addEventListener('DOMContentLoaded', function() {
  const myFile = document.getElementById('myFile');

  const fileChosen = document.getElementById('file-chosen');

  myFile.addEventListener('change', function(){
    fileChosen.textContent = this.files[0].name
  })
});