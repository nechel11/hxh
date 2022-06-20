package main

import (
	"fmt"
	"html/template"
	"net/http"
	
)


func index(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/index.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "index", nil)
}

func create(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/create.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "create", nil)
}

func contacts(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/contacts.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "contacts", nil)
}

func login(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/login_form.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "login_form", nil)
}

func registerauth(w http.ResponseWriter, r *http.Request){
	nick := r.FormValue("username")
	password := hash_func(r.FormValue("password"))

}

func handleFunc(){
	http.HandleFunc("/", index)
	http.HandleFunc("/contacts/", contacts)
	http.HandleFunc("/create/", create)
	http.HandleFunc("/login/", login)
	http.HandleFunc("/registerauth/", registerauth)
	http.ListenAndServe(":8080", nil)
}

func main(){
	handleFunc()
}