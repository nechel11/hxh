package contacts

import (
	"fmt"
	"html/template"
	"net/http"
	
)

func Contacts(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseFiles("templates/contacts.html", "templates/header.html")
	if err != nil {
		fmt.Fprintf(w, err.Error())
	}
	tmpl.ExecuteTemplate(w, "contacts", nil)
}