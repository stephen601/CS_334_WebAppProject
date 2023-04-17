window.onload = function(){
    loginButton = document.getElementById('loginButton');

    loginButton.addEventListener("click", function(){

        theUsername = document.getElementById("inputUsername").value;
        thePassword = document.getElementById("inputPassword").value;

        console.log(theUsername);

        fetch('./users.json')
                    .then((response) => response.json())
                    .then((orderElements) => {

                        foundUser = false;

                        for(let i=0; i<orderElements.length; i++){

                            if(theUsername == orderElements[i].username){

                                foundUser = true;

                                if(thePassword == orderElements[i].password){

                                    window.location.replace("./manager.html");

                                }
                                else{

                                    alert("Invalid Credentials, please try again.");

                                }

                            }
                            else{

                            }

                        }

                        if(!foundUser){
                            alert("Invalid Credentials, please try again.");
                        }
                        else{

                        }



                    });

    })
}