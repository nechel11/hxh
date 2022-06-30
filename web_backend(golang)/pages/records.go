package pages

import (
	"fmt"
	"html/template"
	"net/http"
	"../db"
)

func Records(w http.ResponseWriter, r *http.Request){
	tmpl, _ := template.ParseFiles("templates/records.html", "templates/header.html")
	records := *db.User_records(db.User.Telegram_nick)

	if len(records) == 0{
		tmpl.ExecuteTemplate(w, "records", nil)
	} else {
		tmpl.ExecuteTemplate(w, "records", records)
		return
	}
	fmt.Println("db. user", db.User)
	fmt.Println("records", records)

}