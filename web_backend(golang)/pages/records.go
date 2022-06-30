package pages

import (
	"fmt"
	"html/template"
	"net/http"

	"../db"
	"github.com/gorilla/mux"
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

func Show_records (w http.ResponseWriter, r *http.Request){
	tmpl, _ := template.ParseFiles("templates/one_record.html", "templates/header.html")
	vars := mux.Vars(r)
	w.WriteHeader(http.StatusOK)
	res := db.Get_one_record(vars["id"])
	tmpl.ExecuteTemplate(w, "one_record", res)
}