
//#region Variables
indexes = ["",
    "address",
    "billinginformation",
    "cart",
    "cartedproduct",
    "customer",
    "neworder",
    "product",
    "staff",
    "wholesaler"
]
address = {};
addressColumns = ["ID", "Street", "City", "aState", "Zip"];
billinginformation={};
billinginformationColumns = ["BillingInformationID", "CreditCardNumber", "ExpirationDate", "AddressID"]
cart = {};
cartColumns = ["CartID","NumberOfItems","TotalCost","ShippingCost","CustomerID"]
cartedproduct = {};
cartedproductColumns = ["CartedProductID","ProductID","CartID"]
customer = {};
customerColumns = ["CustomerID","Email","cName","Pass","AddressID","BillingInformationID"]
neworder = {};
neworderColumns = ["NewOrderID","CartID","StaffID","OrderDate"]
product = {};
productColumns = ["ProductID","ShippingCost","ProductName","Color","Price","WholesalerID"]
staff = {};
staffColumns = ["StaffID","StaffName","Email","Wage","sPassword"]
wholesaler = {};
wholesalerColumns = ["WholesalerID","Website","WholesalerName","WholesalerPhone","WholesalerLocation"]
//#endregion

function getstuff() {
    $.ajax({
        url: '/api/address',
        type: 'GET',
        success: function(result) {
            address = result;
        }
    });
    $.ajax({
        url: '/api/billinginformation',
        type: 'GET',
        success: function(result) {
            billinginformation = result;
        }
    });
    $.ajax({
        url: '/api/cart',
        type: 'GET',
        success: function(result) {
            cart = result;
        }
    });
    $.ajax({
        url: '/api/cartedproduct',
        type: 'GET',
        success: function(result) {
            cartedproduct = result;
        }
    });
    $.ajax({
        url: '/api/customer',
        type: 'GET',
        success: function(result) {
            customer = result;
        }
    });
    $.ajax({
        url: '/api/neworder',
        type: 'GET',
        success: function(result) {
            neworder = result;
        }
    });
    $.ajax({
        url: '/api/product',
        type: 'GET',
        success: function(result) {
            product = result;
        }
    });
    $.ajax({
        url: '/api/staff',
        type: 'GET',
        success: function(result) {
            staff = result;
        }
    });
    $.ajax({
        url: '/api/wholesaler',
        type: 'GET',
        success: function(result) {
            wholesaler = result;
        }
    });
}
getstuff();

function CreateTableFromJSON(newJson, col, type) {
    getstuff();
    // CREATE DYNAMIC TABLE.
    col.push("Delete", "Edit")
    var table = document.createElement("table");
    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.
    var tr = table.insertRow(-1); // TABLE ROW.
    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th"); // TABLE HEADER.
        th.innerHTML = col[i];
        tr.appendChild(th);
    }
    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < newJson.length; i++) {
        tr = table.insertRow(-1);
        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            if (j == col.length - 1) {
                var intext =  i + ", " + type;
                tabCell.innerHTML = "<button onclick='editRow(" + intext + ")' class='editbtn'>edit</button>"
            } else if (j == col.length - 2) {
                var intext =  newJson[i][0] + ", " + type;
                tabCell.innerHTML = "<button onclick='delRow(" + intext + ")'class='delbtn'>delete</button>"
            } else {
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
    CreateTableFromJSON(address, addressColumns, 1);
}

function editRow(id, type) {
    //add modal here
    $("#editDialog").empty()
    $("#editDialog").append("<form id='editForm'>")
    if(indexes[type] == "address"){
        var t = 0;
         address[id].forEach(element => {
            if(t != 0){
                $("#editForm").append("<label>"+addressColumns[t]+"</label>")
                $("#editForm").append("<input value='"+element+"'name='"+addressColumns[t]+"'type='text'>")
            }
            t++;
         });
    }
    $("#editDialog").append("</form>");
    $("#editDialog").append("<input type='button' onclick='putRow("+id+","+type+")' value='Submit'>");
    $("#editDialog").dialog();
    
}
function putRow(id, type) {
    var newdata = $('#editForm').serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});
    newdata = JSON.stringify(newdata);
    $.ajax({
        url: '/api/' + indexes[type] + '/' + id,
        type: 'PUT',
        data: newdata,
        contentType: "application/json",
        success: function(result) {
            console.log(result);
        }
    });
    $('#editDialog').dialog('close');
    $('#editDialog').empty();
}

function delRow(id, type) {
    $.ajax({
        url: '/api/' + indexes[type] + '/' + id,
        type: 'DELETE',
        success: function(result) {
            console.log(result);
        }
    });
}

function addRow(type){
    $('#addDialog').empty();
    $("#addDialog").append("<form id='addForm'>");
    if(indexes[type] == "address"){
        addressColumns.forEach(element => {
        if(element != "ID"){
            if (element != "Edit"){
                if (element != "Delete"){
                    $("#addForm").append("<label>"+element+"</label>");
                    $("#addForm").append("<input name='"+element+"' value='' type='text'>");
                }
            }
        }
        })
        
    }
    $("#addDialog").append("<input type='button' onclick='postRow("+type+")' value='Submit'>")
    $("#addDialog").css("visibility", "visible");
    $("#addDialog").dialog();
}


// function addAddress() {
//     $("#addDialog").append("<form id='addForm'><label>Street</label><input name='Street' value='' type='text'><label>City</label><input name='City' value='' type='text'><label>aState</label><input name='aState' value='' type='text'><label>zip</label><input name='Zip' value='' type='text'></form><input type='button' onclick='postAddress()' value='Submit'>");
//     $("#addDialog").css("visibility", "visible");
//     $("#addDialog").dialog();
// }
function postRow(type) {
    var newdata = $('#addForm').serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});
    if(indexes[type]=="address"){
        newdata.id = (address[address.length - 1][0] + 1);
    }
    newdata = JSON.stringify(newdata);
    $.ajax({
        url: '/api/' + indexes[type],
        type: 'POST',
        contentType: "application/json",
        data: newdata,
        success: function(result) {
            console.log(result);
        }
    });

    $('#addDialog').dialog('close');
    
}

