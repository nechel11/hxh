package pages

import (
	"fmt"
	"html/template"
	"net/http"
)

func Create(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/create.html", "templates/header.html")
	if err != nil {
		fmt.Fprint(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "create", nil)
}