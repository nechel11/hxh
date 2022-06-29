package pages

import (
	"fmt"
	"html/template"
	"net/http"
	"../utils"
	_ "github.com/lib/pq"
	"../db"
)

type User struct {
	User_id int `json:"user_id"`
	Telegram_id int `json:"telegram_id"`
	Telegram_nick string `json:"telegram_nick"`
	Telegram_password string `json:"telegram_password"`
	Is_user bool 
	
}

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
	fmt.Println(is_user)
	
	if !is_user.Is_user{
		tmpl, _ := template.ParseFiles("templates/login.html", "templates/header.html")
		tmpl.ExecuteTemplate(w, "login", "check username and password")
	} else {
		tmpl, _ := template.ParseFiles("templates/loginauth.html", "templates/header.html")
		is_authenticated:=true
		tmpl.ExecuteTemplate(w, "loginauth", is_authenticated)
	}
	
}