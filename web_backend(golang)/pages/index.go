package pages

import (
	"fmt"
	"html/template"
	"net/http"
)

func Index(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/index.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "index", nil)
}