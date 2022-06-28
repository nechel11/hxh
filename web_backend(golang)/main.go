package main

import (
	"fmt"
	"net/http"
	"database/sql"
	_ "github.com/lib/pq"
	"./pages"
)

const  (
	host = "127.0.0.1" 
	port=5432
	dbname="hxh"
	user = "zafar"
	password="12344321"
)

func main(){
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		panic(err)
	}
	defer db.Close()
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



