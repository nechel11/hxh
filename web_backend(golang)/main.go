package main

import (
	"net/http"

	"./pages"
	"github.com/gorilla/mux"
)

func main(){

	handleFunc()
}

func handleFunc(){
	rtr := mux.NewRouter()
	rtr.HandleFunc("/", pages.Index).Methods("GET")
	rtr.HandleFunc("/create", pages.Create).Methods("GET")
	rtr.HandleFunc("/contacts", pages.Contacts).Methods("GET")
	rtr.HandleFunc("/login", pages.LoginHandler).Methods("GET")
	rtr.HandleFunc("/records", pages.Records).Methods("GET")
	rtr.HandleFunc("/records/{id:[0-9]+}", pages.Show_records).Methods("GET")
	rtr.HandleFunc("/loginauth", pages.LoginAuth)
	rtr.HandleFunc("/logout", pages.LogoutHandler).Methods("GET")
	http.Handle("/", rtr)
	http.ListenAndServe("localhost:8070", nil)
}



