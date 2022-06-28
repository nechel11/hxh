package pages

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
)

type User_info struct {
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

type User struct {
	User_id int `json:user_id`
	Telegram_id int `json:telegram_id`
	Telegram_nick string `json:telegram_nick`
	Telegram_password string `json:telegram_password`
}

const  (
	host = "127.0.0.1" 
	port=5432
	dbname="hxh"
	user = "zafar"
	password="12344321"
)

func if_user(username, password, hash string)  {
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		panic(err)
	}
	defer db.Close()
	is_user, err := db.Query(fmt.Sprintf("Select telegram_nick,telegram_password from users where telegram_nick='%s'", username))
	if err != nil {
		panic(err)
	}
	fmt.Println(is_user)
	for is_user.Next(){
		var user User
		err = is_user.Scan(&user.Telegram_nick, &user.Telegram_password)
		if err != nil {
			panic(err)
			}
		fmt.Printf(fmt.Sprintf("FK: %s with proff %s\n", user.Telegram_nick, user.Telegram_password))
	}

}

