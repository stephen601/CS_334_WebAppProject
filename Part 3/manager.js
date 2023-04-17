window.onload = function(){
    const editButtons = document.getElementsByClassName("editButton");
    const deleteButtons = document.getElementsByClassName("deleteButton");
    const addFlavorButton = document.getElementById('addFlavor');

    const refundOrderButtons = document.getElementsByClassName("refundOrder");
    const viewOrderButtons = document.getElementsByClassName("viewOrder");

    // Add Icecream
    addFlavorButton.addEventListener("click", function() {

        newIcecreamName = prompt("What should the name be? ");
        if(newIcecreamName === null){
            return;
        }
        else{
            newIcecreamPrice = prompt("What should the price be?");
            if(newIcecreamPrice === null){
                return;
            }
            else{
                // All new icecreams default to the image of chocolate icecream.
                localStorage.setItem(newIcecreamName, JSON.stringify([newIcecreamPrice, "./images/chocolate.jfif", true]));
                window.location.reload();
            }
        }

    });


    // Edit Icecream:
    for(let i = 0; i < editButtons.length; i++){
        editButtons[i].addEventListener("click", function() {

            // Get type of icecream by ID
            iceCreamType = deleteButtons[i].id;

            // Fix icecream name
            lastIndex = iceCreamType.lastIndexOf(" ");
            iceCreamType = iceCreamType.substring(0, lastIndex);

            newPrice = prompt("Enter the new price: ");
            if(newPrice === null){
                return;
            }
            else{
                console.log(iceCreamType);
                theImage = JSON.parse(localStorage.getItem(iceCreamType))[1];

                localStorage.setItem(iceCreamType, JSON.stringify([newPrice, theImage, true]));

                priceElement = document.getElementById(iceCreamType + ' price');
                priceElement.innerHTML = '$' + newPrice;
            }
            

        });
    }

    // Delete Icecream: 
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

    // View Order Buttons
    for(let i = 0; i < viewOrderButtons.length; i++){
        viewOrderButtons[i].addEventListener("click", function(){

            specificOrder = viewOrderButtons[i].id;

            lastIndex = specificOrder.lastIndexOf(" ");
            specificOrder = specificOrder.substring(0, lastIndex);

            specificOrder = specificOrder.toString();
            
            fetch('./orders.json')
                .then((response) => response.json())
                .then((orderElements) => {

                    for(let j=0; j<orderElements.length; j++){
                        if(specificOrder == orderElements[j].id){
                            console.log("Item Viewed");
                            alert(orderElements[j].items);
                        }
                        else{

                        }
                    }

                });

        })
    }

    // Refund Order Buttons
    for(let i = 0; i < refundOrderButtons.length; i++){
        refundOrderButtons[i].addEventListener("click", function(){

            specificOrder = viewOrderButtons[i].id;

            lastIndex = specificOrder.lastIndexOf(" ");
            specificOrder = specificOrder.substring(0, lastIndex);

            specificOrder = specificOrder.toString();
            
            fetch('./orders.json')
                .then((response) => response.json())
                .then((orderElements) => {

                    for(let j=0; j<orderElements.length; j++){
                        if(specificOrder == orderElements[j].id){
                            console.log("Refund Initiated");
                            confirmation = confirm("Are you sure you want to refund this order?");
                            if(confirmation == false){
                                return;
                            }
                            else{
                                alert("Order refunded.");
                            }
                        }
                        else{

                        }
                    }

                });

        })
    }
}