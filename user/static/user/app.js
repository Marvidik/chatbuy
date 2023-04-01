var year = document.getElementById('year')
function dateInput(){
   return new Date().getFullYear()
}
year.innerHTML = dateInput();
