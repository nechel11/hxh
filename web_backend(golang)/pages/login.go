package pages

import (
	"fmt"
	"html/template"
	"net/http"
	"../utils"
	_ "github.com/lib/pq"
	"../db"
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
	hash := utils.To_hash(password)
	fmt.Println("username:", username, "password:", password, hash)
	
	is_user := db.If_user(username, password, hash)
	records := *db.User_records(username)
	fmt.Println(records[0].Vacancy)
	if !is_user.Is_user{
		tmpl, _ := template.ParseFiles("templates/login.html", "templates/header.html")
		tmpl.ExecuteTemplate(w, "login", "check username and password")
	} else {
		tmpl, _ := template.ParseFiles("templates/records.html", "templates/header.html")
		tmpl.ExecuteTemplate(w, "records", records)
	}
	
}