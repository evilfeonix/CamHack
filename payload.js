var local = {
    error: "Unidentified",
    Country: "Nigeria",
    languages: "en",
}

var x;
x=prompt("Enter Your Full Name Here\n\n👇👇👇👇👇");

            function force(){
                if (x==null || x=="" || x==" " || x=="  " || x=="   "|| x=="    " || x=="     "){
                    console.log("omo!, you get sence"); 
                    x=prompt("Please Enter Your Full Name, Abeg!...\n\n👇👇👇👇👇");
                    force();
                }else{console.log("hmm, i even think say you get sence");}
            }

            force();  
        // getFullYear.innerHTML = new Date().getFullYear();
 
            var xxx=x;
        
        
                function wait4me(t){return new Promise((r)=>setTimeout(r,t));}
               
