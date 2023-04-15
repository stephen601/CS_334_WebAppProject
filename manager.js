window.onload = function(){
    const editButtons = document.getElementsByClassName("editButton");
    const deleteButtons = document.getElementsByClassName("deleteButton");
    const addFlavorButton = document.getElementById('addFlavor');

    // addFlavorButton.addEventListener("click", function() {



    // })


    for(let i = 0; i < editButtons.length; i++){
        editButtons[i].addEventListener("click", function() {

            // Get type of icecream by ID
            iceCreamType = editButtons[i].id.split(" ");

            // If the icecream name has a space in it, fix it
            if(iceCreamType.length > 2){
                iceCreamType = iceCreamType[0] + ' ' + iceCreamType[1];
            }
            else{
                iceCreamType = iceCreamType[0];
            }

            newPrice = prompt("Enter the new price: ");
            if(newPrice === null){
                return;
            }
            else{
                theImage = JSON.parse(localStorage.getItem(iceCreamType))[1];

                localStorage.setItem(iceCreamType, JSON.stringify([newPrice, theImage, true]))

                priceElement = document.getElementById(iceCreamType + ' price');
                priceElement.innerHTML = '$' + newPrice;
            }
            

        });
    }



    // Note that we can't delete the icecream from local storage.
    // If that happens, then the icecream will be regenerated in manager.html
    for(let i = 0; i < deleteButtons.length; i++){
        deleteButtons[i].addEventListener("click", function(){

            // Get type of icecream by ID
            iceCreamType = deleteButtons[i].id;

            // Fix icecream name
            lastIndex = iceCreamType.lastIndexOf(" ");
            iceCreamType = iceCreamType.substring(0, lastIndex);

            confirmation = confirm("Are you sure you want to delete this?");
            if(confirmation == false){
                return;
            }
            else{
                thePrice = JSON.parse(localStorage.getItem(iceCreamType))[0];
                theImage = JSON.parse(localStorage.getItem(iceCreamType))[1];

                localStorage.setItem(iceCreamType, JSON.stringify([thePrice, theImage, false]));

                var toDelete = document.getElementById(iceCreamType + ' card');
                toDelete.remove();

                // This reload resolves a bug.
                window.location.reload();
            }
        })
    }
}