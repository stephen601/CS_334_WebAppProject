window.onload = function(){
    
    setTimeout(function(){
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

                    const formData = new URLSearchParams();

                    formData.append('name', newIcecreamName);
                    formData.append('price', newIcecreamPrice);
                    formData.append('image', './images/chocolate.jfif');

                    fetch("https://teamcs334.pythonanywhere.com/ice_cream",
                    {
                        method: "POST",
                        body: formData
                        
                    }).then(res => {
                        console.log("Request complete! response:", res);
                        window.location.reload();
                    });

                }
            }

        });

        
        // Edit Icecream:
        for(let i = 0; i < editButtons.length; i++){
            editButtons[i].addEventListener("click", function() {
                
                // Get type of icecream by ID
                iceCreamType = editButtons[i].id;

                // Fix icecream name
                lastIndex = iceCreamType.lastIndexOf(" ");
                iceCreamType = iceCreamType.substring(0, lastIndex);

                newPrice = prompt("Enter the new price: ");
                if(newPrice === null){
                    return;
                }
                else{

                    let theURL = "https://teamcs334.pythonanywhere.com/ice_cream";
                    var desiredImage = "";
                    var iceCreamID = "";

                    fetch(theURL)
                     .then(res => res.json())
                     .then((iceCreamJSON) => {

                        for (let item of iceCreamJSON){
                            if(item.name == iceCreamType){
                                console.log('here');
                                var desiredImage = item.image;
                                var iceCreamID = item.id;

                                var theFetchURL = "https://teamcs334.pythonanywhere.com/ice_cream/"+ iceCreamID;

                                const formData = new URLSearchParams();

                                formData.append('name', iceCreamType);
                                formData.append('price', newPrice);
                                formData.append('image', desiredImage);


                                fetch(theFetchURL,
                                {
                                    method: "PUT",
                                    body: formData
                                
                                }).then(res => {
                                    console.log("Request complete! response:", res);
                                    window.location.reload();
                                });

                            }
                        }
                     });

                     
                    
                }
                

            });
        }
        
        // Delete Icecream: 
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

                    let theURL = "https://teamcs334.pythonanywhere.com/ice_cream";
                    var iceCreamID = "";

                    fetch(theURL)
                     .then(res => res.json())
                     .then((iceCreamJSON) => {
                        for (let item of iceCreamJSON){
                            if(item.name == iceCreamType){
                                let iceCreamID = item.id;

                                const formData = new URLSearchParams();

                                var theFetchURL = "https://teamcs334.pythonanywhere.com/ice_cream/"+ iceCreamID;
                                fetch(theFetchURL,
                                {
                                    method: "DELETE"
                                
                                }).then(res => {
                                    console.log("Request complete! response:", res);
                                    window.location.reload();
                                });

                            }
                        }
                     });

                    
                    
                }
            })
        }
        
        // View Order Buttons
        for(let i = 0; i < viewOrderButtons.length; i++){
            viewOrderButtons[i].addEventListener("click", function(){
                
                specificOrderID = viewOrderButtons[i].id;

                lastIndex = specificOrderID.lastIndexOf(" ");
                specificOrderID = specificOrderID.substring(0, lastIndex);
                specificOrderID = specificOrderID.toString();
                
                fetch("https://teamcs334.pythonanywhere.com/orders/"+specificOrderID)
                    .then((response) => response.json())
                    .then((orderElements) => {
                        console.log(orderElements);
                        console.log(orderElements.ice_cream.name);
                        alert(orderElements.quantity + ' ' + orderElements.ice_cream.name);

                    });

            })
            
        }
        
        // Refund Order Buttons
        for(let i = 0; i < refundOrderButtons.length; i++){
            refundOrderButtons[i].addEventListener("click", function(){

                // specificOrder = viewOrderButtons[i].id;

                // lastIndex = specificOrder.lastIndexOf(" ");
                // specificOrder = specificOrder.substring(0, lastIndex);

                // specificOrder = specificOrder.toString();
                
                

                console.log("Refund Initiated");
                confirmation = confirm("Are you sure you want to refund this order?");
                if(confirmation == false){
                    return;
                }
                else{
                    alert("Order refunded.");
                }

                    

            })
        }
    }, 1000);
}