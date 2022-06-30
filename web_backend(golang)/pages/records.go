package pages

import (
	// "fmt"
	"html/template"
	"net/http"
	"../db"
)

func Records(w http.ResponseWriter, r *http.Request){
	tmpl, _ := template.ParseFiles("templates/records.html", "templates/header.html")
	// records := *db.User_records(User_db.Telegram_nick)
	// fmt.Println(records[0].Vacancy)
	rc := db.User_records("nechel1233")
	tmpl.ExecuteTemplate(w, "records", rc)

}