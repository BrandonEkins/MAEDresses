var value = $.get("/api/address");
function CreateTableFromJSON(newJson, col, type) {
    // CREATE DYNAMIC TABLE.
    col.push("Delete","Edit")
    var table = document.createElement("table");
    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.
    var tr = table.insertRow(-1);                   // TABLE ROW.
    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // TABLE HEADER.
        th.innerHTML = col[i];
        tr.appendChild(th);
    }
    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < newJson.length; i++) {
        tr = table.insertRow(-1);
        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            if(j == col.length -1){
                tabCell.innerHTML = "<button onclick='editRow("+newJson,i,type+")' class='editbtn'>edit</button>"
            }
            else if(j == col.length -2){
                tabCell.innerHTML = "<button onclick='delRow("+i, type+")'class='delbtn'>delete</button>"
            }
            else{
                tabCell.innerHTML = newJson[i][j];
            }
        }
    }
    // TODO: create edit section
    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById("showData");
    divContainer.innerHTML = "";
    divContainer.appendChild(table);
}
function AddressTable() {
    CreateTableFromJSON(value.responseJSON, ["ID","Street", "City", "nState", "Zip"], "Address");
}
function editRow(newJson,id,type) {
    //add modal here
    $.ajax({
        url: '/api/'+type+'/'+id,
        type: 'PUT',
        data: "",
        success: function(result) {
            console.log(result);
        }
    });
}
function delRow(id, type){
    //add modal here
    $.ajax({
        url: '/api/'+type+'/'+id,
        type: 'DELETE',
        success: function(result) {
            console.log(result);
        }
    });
}
function addRow(type){
    $( "#addDialog" ).dialog();
    
    $.ajax({
        url: '/api/'+type,
        type: 'POST',
        data: "",
        success: function(result) {
            console.log(result);
        }
    }); 
}
