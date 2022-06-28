package main

import (
	"net/http"
	_ "github.com/lib/pq"
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
	http.HandleFunc("/loginauth", pages.LoginAuth)
	http.ListenAndServe("localhost:8070", nil)
}



