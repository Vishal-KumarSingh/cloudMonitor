/*
This file includes bunch of libraries to perform sreverl operation in the cloud monitor tool 



*/



var files = [];
function updateTable(){
document.querySelector('tbody').innerHTML = '';
for(var i=1; i<files.length; i++){
  var splittedcontent = files[i].split(' ');
  var text = ``;
  var tr = document.createElement('tr');
  document.querySelector('tbody').appendChild(tr);
  tr.appendChild(document.createElement('td')).innerText = i;
  tr.classList.add('files');
  var count = 0;
  var pid = 0;
  for(var j=0; j<splittedcontent.length; j++){

   
    

    if(splittedcontent[j].length > 0){
      if((++count) > 11){
       break;
      }
      if(count == 2){
           pid = splittedcontent[j];
      }
      tr.appendChild(document.createElement('td')).innerText = splittedcontent[j];
    }

  }
  tr.id = pid;
   tr.addEventListener('click', function(e){
       openDialog(this.id);
  });
  
  // console.log(file);
}
}
function loadLocation(){
 fetchData("{% url 'taskmanagerapi' %}", {} , (data) => {
    console.log(data);
    //$("#window").append(data);
    files = JSON.parse(data);
    updateTable();
});
}

function openDialog(id) {



Swal.fire({
title: "Do you want to kill this Process?",
text: "This process will be terminated",
icon: "warning",
showCancelButton: true,
confirmButtonColor: "#3085d6",
cancelButtonColor: "#d33",
confirmButtonText: "Yes, delete it!"
}).then((result) => {
if (result.isConfirmed) {


fetchData("{% url 'killprocess' %}", {id: id} , (data) => {
 Swal.fire({
 title: "Killed !!",
 text: "Process has been terminated.",
 icon: "success"
});
 });


}
});
}








