function showCashOption() {
        // hide card information input field
        document.getElementById("card-info").style.display = "none";
      }
    
      function showCardOption() {
        // show card information input field
        document.getElementById("card-info").style.display = "block";
      }
    fetch("iceCream.json")
    .then(response => response.json())
    .then(data => {
      for (let i = 0; i < data.length; i++) {
        console.log(data[i].Name, data[i].cost, data[i].iceCream);
        document.querySelector(`#name${i}`).innerText = data[i].Name;
        document.querySelector(`#cost${i}`).innerText= parseFloat(data[i].cost).toFixed(2);
        document.getElementById(`iceCream${i}`).src = data[i].iceCream;
      }
    });
