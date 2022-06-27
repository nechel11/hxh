package login

import (
	"fmt"
	"html/template"
	"net/http"
	"./hash_func"

	
)

func LoginHandler(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/login_form.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	fmt.Println("*****loginHandler running*****")
	tmpl.ExecuteTemplate(w, "login_form", nil)
}

func Registerauth(w http.ResponseWriter, r *http.Request){
	fmt.Println("*****loginAuthHandler running*****")
	r.ParseForm()
	username := r.FormValue("username")
	password := r.FormValue("password")
	fmt.Println("username:", username, "password:", password)
	hash := hash_func.To_hash(password)
	fmt.Println(hash)
	// stmt := "SELECT password FROM users WHERE telegram_nick=(%s)"
}