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

func save_article(w http.ResponseWriter, r *http.Request){
	title := r.FormValue("title")
	anons := r.FormValue("anons")
	full_text := r.FormValue("full_text")
}


func handleRequest(){
	http.HandleFunc("/", index)
	http.HandleFunc("/contacts/", contacts)
	http.HandleFunc("/create/", create)
	http.ListenAndServe(":8080", nil)
}

func main(){
	handleRequest()
}