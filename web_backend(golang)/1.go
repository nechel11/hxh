package main

import (
	"html/template"
	"net/http"
	"database/sql"
	"github.com/jackc/pgx/v4"
)

type User struct {
	Name string
	Age uint16
	Money int16
	Avg_grades, Happiness float64
	Hobbies []string
}

type Contacts struct {
	Name string
	Telegram string
	Hh_id string
}


func home_page(w http.ResponseWriter, r *http.Request){
	bob := User{"Bob", 25, 10, 3.7, 0.8, []string{"footbal", "Skate"}}
	tmpl, _ := template.ParseFiles("templates/home_page.html")
	tmpl.Execute(w, bob)
}

func contacts_page(w http.ResponseWriter, r *http.Request){
	contacts := Contacts{"Zafar Khasanov", "https://t.me/nechel1233", "https://hh.ru/resume/fe3d9308ff0727aa460039ed1f336b6276536e"}
	tmpl, _ := template.ParseFiles("templates/contacts.html")
	tmpl.Execute(w, contacts)
}

func handleRequest(){
	http.HandleFunc("/", home_page)
	http.HandleFunc("/contacts/", contacts_page)
	http.ListenAndServe(":8080", nil)
}

func main(){
	
	handleRequest()
}