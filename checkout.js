function showCashOption() {
    // hide card information input field
    document.getElementById("card-info").style.display = "none";
    // show cash button
    document.getElementById("cash-button").style.display = "block";
    // reset margin of payment-options
    document.getElementById("payment-options").style.marginBottom = "20px";
}


function showCardOption() {
    // show card information input field
    document.getElementById("card-info").style.display = "block";
    // hide cash button
    // document.getElementById("cash-button").style.display = "none";
    // adjust margin of payment-options to make space for card-info
    document.getElementById("payment-options").style.marginBottom = "100px";
}

function submitForm() {
    // Redirect to payment success page
    window.location.href = "payment_success.html";
}


// Define function to update the total
function updateTotal() {
    let total = 0;
    const itemElements = document.querySelectorAll('.item');
    itemElements.forEach((itemElement, i) => {
        const quantityElement = document.getElementById(`quantity${i}`);
        const quantity = parseInt(quantityElement.value);
        const priceElement = itemElement.querySelector('.item-price');
        const price = parseFloat(priceElement.innerText.slice(1));
        const subtotal = quantity * price;
        total += subtotal;
    });
    const totalElement = document.getElementById('total');
    totalElement.innerHTML = `Total: $${total.toFixed(2)}`;
}



// Define function to generate HTML for items
function generateItemsHtml(iceCreamItems) {
    let html = '';
    let total = 0;
    for (let i = 0; i < iceCreamItems.length; i++) {
        const itemPrice = iceCreamItems[i].price.toFixed(2);
        total += parseFloat(itemPrice);
        html += `
            <div class="item">
    <div style="display:inline-block;"><img src="${iceCreamItems[i].imageSrc}" /></div>
    <div class="item-info">
        <div class="item-name" id="name${i}">${iceCreamItems[i].name}</div>
        <div class="item-price" id="price${i}">$${itemPrice}</div>
        <div class="item-quantity">
            <label for="quantity${i}">Quantity:</label>
            <input type="number" id="quantity${i}" name="quantity" min="1" max="10" value="${initialQuantities[i]}">
        </div>

        <div class="subtotal"></div>
    </div>
</div>

        `;
    }
    html += `<div id="total">Total: $${total.toFixed(2)}</div>`;
    return html;
}

// Define array of test ice cream items
// Define array of test ice cream items
const testIceCreamItems = [0, 2, 4, 5];
const initialQuantities = [1, 1, 2, 4];


// Fetch ice cream data from JSON file
fetch('iceCream.json')
    .then(response => response.json())
    .then(data => {
        // Filter the ice cream items to display
        const itemsToDisplay = data.filter((item, index) => testIceCreamItems.includes(index));
        // Generate HTML for the ice cream items
        const itemsHtml = generateItemsHtml(itemsToDisplay);
        // Insert the HTML into the DOM
        const itemsContainer = document.getElementById('items-container');
        if (itemsContainer) {
            itemsContainer.innerHTML = itemsHtml;
            // Add event listeners to each quantity input field
            const quantityInputs = document.querySelectorAll('.item-quantity input');
            quantityInputs.forEach((input, index) => {
                input.addEventListener('input', () => {
                    // Update the subtotal and total
                    updateTotal();
                });
            });
            // Call updateTotal() initially to calculate the total for the default quantities
            updateTotal();
        

        }
    })
    .catch(error => {
        console.log('Error fetching ice cream data:', error);
    });
