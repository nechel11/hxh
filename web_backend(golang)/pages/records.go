package pages

import (
	"fmt"
	"html/template"
	"net/http"
)

func Records(w http.ResponseWriter, r *http.Request){
	tmpl, _ := template.ParseFiles("templates/records.html", "templates/header.html")
	tmpl.ExecuteTemplate(w, "records", nil)
	fmt.Println("RECORDS")

}