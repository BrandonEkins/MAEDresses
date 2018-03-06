var value = $.get("/api/address");
function CreateTableFromJSON(newJson, col, type) {
    // CREATE DYNAMIC TABLE.
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
                tabCell.innerHTML = "<button onclick='editRow("+newJson, col+")' class='editbtn'>edit</button>"
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
    CreateTableFromJSON(value.responseJSON, ["ID","Street", "City", "nState", "Zip","Delete","Edit"], "Address");
}
function editRow() {

}
function delRow(){

}
$(document).ready(function(){
    $('.editbtn').click(function(){
        $(this).html($(this).html() == 'edit' ? 'modify' : 'edit');
    });
});