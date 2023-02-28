fetch("iceCream.json")
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.length; i++) {
      console.log(data[i].Name, data[i].iceCream);
      document.querySelector(`#name${i}`).innerText = data[i].Name;
      document.getElementById(`iceCream${i}`).src = data[i].iceCream;
    }
  });


