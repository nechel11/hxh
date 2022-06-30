package pages

import (
	"fmt"
	"html/template"
	"net/http"
	_ "github.com/lib/pq"
	 "../db"
)

func LogoutHandler(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/logout.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	db.User = db.User_struct{}
	db.Recs = []db.User_info{}
	tmpl.ExecuteTemplate(w, "logout", nil)
}