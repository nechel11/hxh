package pages

import (
	"fmt"
	"html/template"
	"net/http"
	// "../utils"
)

func LoginHandler(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/login.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "login", nil)

}

func LoginAuth(w http.ResponseWriter, r *http.Request){
	fmt.Println("*****loginAuthHandler running*****")
	r.ParseForm()
	username := r.FormValue("username")
	password := r.FormValue("password")
	fmt.Println("username:", username, "password:", password)
}