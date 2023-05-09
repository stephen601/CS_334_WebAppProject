window.onload = function(){
    loginButton = document.getElementById('loginButton');

    loginButton.addEventListener("click", function(){

        theUsername = document.getElementById("inputUsername").value;
        thePassword = document.getElementById("inputPassword").value;

        console.log(theUsername);

        theURL = "https://teamcs334.pythonanywhere.com/user";

        fetch(theURL)
                    .then((response) => response.json())
                    .then((orderElements) => {

                        let foundAdmin = false;
                        let foundUser = false;


                            for(let i=0; i<orderElements.length; i++){

                                if(orderElements[i].is_admin == 1){

                                    foundAdmin = true;

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
                                else{

                                }

                                

                            }

                            if(!foundUser || !foundAdmin){
                                alert("Invalid Credentials, please try again.");
                            }
                            else{

                            }
                        
                    });

    })
}