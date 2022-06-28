package pages

import (
	"fmt"
	"html/template"
	"net/http"
	"../utils"
)

func LoginHandler(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/login_form.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	fmt.Println("*****loginHandler running*****")
	tmpl.ExecuteTemplate(w, "login_form", nil)
}

func LoginAuth(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/loginauth.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	fmt.Println("*****loginAuthHandler running*****")
	r.ParseForm()
	username := r.FormValue("username")
	password := r.FormValue("password")
	fmt.Println("username:", username, "password:", password)
	hash := utils.To_hash(password)
	fmt.Println(hash)
	tmpl.ExecuteTemplate(w, "loginauth", nil)
	// stmt := "SELECT password FROM users WHERE telegram_nick=(%s)"
}