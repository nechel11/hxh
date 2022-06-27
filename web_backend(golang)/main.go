package main

import (
	"fmt"
	"html/template"
	"net/http"
	"database/sql"
	_ "github.com/lib/pq"
	"./contacts"
	 "./login"
)

const  (
	host = "127.0.0.1" 
	port=5432
	dbname="hxh"
	user = "zafar"
	password="12344321"
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

func handleFunc(){
	http.HandleFunc("/", index)
	http.HandleFunc("/contacts/", contacts.Contacts)
	http.HandleFunc("/create/", create)
	// http.HandleFunc("/login/", login.LoginHandler)
	// http.HandleFunc("/registerauth/", registerauth)
	http.ListenAndServe(":8080", nil)
}

func main(){
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	handleFunc()
}