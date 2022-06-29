package db

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
)

type User struct {
	User_id int `json:"user_id"`
	Telegram_id int `json:"telegram_id"`
	Telegram_nick string `json:"telegram_nick"`
	Telegram_password string `json:"telegram_password"`
	Is_user bool 
	
}

const  (
	host = "127.0.0.1" 
	port=5432
	dbname="hxh"
	user = "zafar"
	password="12344321"
)

func db_connect() (x *sql.DB){
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		panic(err)
	}
	return db
}

func If_user(username, pass, hash string) *User {
	db := db_connect()
	defer db.Close()
	is_user, err := db.Query(fmt.Sprintf("Select user_id,telegram_id,telegram_nick,telegram_password from users where telegram_nick='%s'", username))
	fmt.Printf("Select telegram_nick,telegram_password from users where telegram_nick='%s'", username)
	if err != nil {
		panic(err)
	}
	for is_user.Next(){
		fmt.Println("entered for loop")
		var user User
		err = is_user.Scan(&user.User_id, &user.Telegram_id,&user.Telegram_nick, &user.Telegram_password)
		if err != nil {
			panic(err)
			}
		if user.Telegram_nick == username && user.Telegram_password == hash{
			user.Is_user = true
			fmt.Printf("user: %s pass %s\n", user.Telegram_nick, user.Telegram_password)
			return &user
		}
	}
	var not_user User
	return &not_user
}
