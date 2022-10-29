function buildTable(){
    addLineToHTMLTable("Ko Nyi","Buffa");
    addLineToHTMLTable("John","Forgue");
    addLineToHTMLTable("Tim","Berners");
}
function addLineToHTMLTable(firstName,lastName){
    //get the body of the table using the selector API
    var tableBody=document.querySelector("#tableContactBody");

    //add a new row at the end of the table

    var newRow=tableBody.insertRow();

    //add new cells to the row

    var firstNameCell=newRow.insertCell();
    firstNameCell.innerHTML=firstName;

    var lastNameCell=newRow.insertCell();
    lastNameCell.innerHTML=lastName;
}