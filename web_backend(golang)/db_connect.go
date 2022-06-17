package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

type User struct {
	Fk_telegram_id int `json:"name"`
	Proff string `json:"proff"`
	Vacancy string `json:"vacancy"`
	Salary_from string `json:"salary_from"`
	Salary_to string `json:"salary_to"`
	Requir string `json:"requir"`
	Respons string `json:"respons"`
	Url string `json:"url"`
	Company string `json:"company"`
	Schedule string `json:"schedule"`
	Vacancy_id string `json:"vacancy_id"`
	Adress string `json:"adress"`
	Currency string `json:"currency"`
}

const  (
	host = "127.0.0.1" 
	port=5432
	dbname="hxh"
	user = "zafar"
	password="12344321"
)

func main() {
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		fmt.Println("ошибка1")
		panic(err)
	}
	defer db.Close()

	res, err := db.Query("Select fk_telegram_id, vacancy FROM  records")
	if err != nil {
		fmt.Println("ошибка2")
		panic(err)
	}
	for res.Next(){
		var user User
		err = res.Scan(&user.Fk_telegram_id, &user.Vacancy)
		if err != nil {
			fmt.Println("ошибка3")
			panic(err)
			}
		fmt.Println(fmt.Sprintf("FK: %d with proff %s", user.Fk_telegram_id, user.Vacancy))
	}

}