package main

import (
	"net/http"
	"./pages"
	 
)

func main(){

	handleFunc()
}

func handleFunc(){
	http.HandleFunc("/", pages.Index)
	http.HandleFunc("/create", pages.Create)
	http.HandleFunc("/contacts", pages.Contacts)
	http.HandleFunc("/login", pages.LoginHandler)
	http.HandleFunc("/records", pages.Records)
	http.HandleFunc("/loginauth", pages.LoginAuth)
	http.HandleFunc("/logout", pages.LogoutHandler)
	http.ListenAndServe("localhost:8070", nil)
}



