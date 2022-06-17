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

func contacts(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/contacts.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "contacts", nil)
}

func handleRequest(){
	http.HandleFunc("/", index)
	http.HandleFunc("/contacts/", contacts)
	http.ListenAndServe(":8080", nil)
}

func main(){
	
	handleRequest()
}