
const demo = document.getElementById('monbouton');
console.log(demo)



demo.addEventListener("click", function () {
    const xhr = new XMLHttpRequest(); // on doit définir un objet qui permet de faire la requete
    const url = "https://api.tisseo.fr/v2/lines.json?key=a3732a1074e2403ce364ad6e71eb998cb"; // donner le lien ou le fichier HTML qui est concerné
    const methode = "GET";// donner la methode qu'on veut (obtenir ou poster ou supprimer des données du serveur ou de l'API)
    xhr.open(methode, url);// la methode permet d'ouvrir une requête
    xhr.responseType = "json"

    
    xhr.onreadystatechange = function() {
        // On vérifie l'état et le statut de la requête
        if (xhr.readyState === 4 && xhr.status === 200) {
            // on stocke les réponses dans un objet reponse
            const reponse = xhr.response; 
            // afficher les noms des lignes sous forme de liste à puces 
            let listeNomsLignes = "<ul>";

                      
                reponse.lines.line.forEach(line => {
                    listeNomsLignes += `<li>${line.name}}</li>`; 
                        
                });
                listeNomsLignes+= "</ul>"

                demo.innerHTML = listeNomsLignes;              
               
        } else if (xhr.readyState === 4) {
                alert("Erreur: " + xhr.status + " - une erreur est survenue!!");
            }
        };
    
    xhr.send();
});


