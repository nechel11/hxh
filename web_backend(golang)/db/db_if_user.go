package db

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
)

type User_struct struct {
	User_id int `json:"user_id"`
	Telegram_id int `json:"telegram_id"`
	Telegram_nick string `json:"telegram_nick"`
	Telegram_password string `json:"telegram_password"`
	Is_user bool 
	
}

type User_info struct {
	Records_id int `json:"records_id"`
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
	Fk_telegram_id int `json:"name"`
}

const  (
	db_host = "127.0.0.1" 
	db_port=5432
	db_name="hxh"
	db_user = "zafar"
	db_password="12344321"
)

func Db_connect() (x *sql.DB){
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", db_host, db_port, db_user, db_password, db_name)
	db, err := sql.Open("postgres", psqconn)
	if err != nil {
		panic(err)
	}
	return db
}

var Recs = []User_info{}
var Show_rec = User_info{}
var User =  User_struct{}

func If_user(username, pass, hash string) *User_struct {
	db := Db_connect()
	defer db.Close()
	is_user, err := db.Query(fmt.Sprintf("Select user_id,telegram_id,telegram_nick,telegram_password from users where telegram_nick='%s'", username))
	fmt.Printf("Select telegram_nick,telegram_password from users where telegram_nick='%s'", username)
	if err != nil {
		panic(err)
	}
	User = User_struct{}
	for is_user.Next(){
		err = is_user.Scan(&User.User_id, &User.Telegram_id,&User.Telegram_nick, &User.Telegram_password)
		if err != nil {
			panic(err)
			}
		if User.Telegram_nick == username && User.Telegram_password == hash{
			User.Is_user = true
			fmt.Printf("user: %s pass %s\n", User.Telegram_nick, User.Telegram_password)
			return &User
		}
	}
	return &User
}

func User_records(username string) *[]User_info{
	db := Db_connect()
	defer db.Close()
	records, err := db.Query(fmt.Sprintf("SELECT records_id,proff, vacancy, salary_from, salary_to, requir, respons, url, company, schedule, vacancy_id, adress, currency, fk_telegram_id FROM records inner join users on users.telegram_id = records.fk_telegram_id WHERE telegram_nick='%s'", username))
	if err != nil {
		panic(err)
}
	Recs = []User_info{}
	for records.Next(){
		var rec_list User_info
		err = records.Scan(&rec_list.Records_id,&rec_list.Proff, &rec_list.Vacancy, &rec_list.Salary_from, 
			&rec_list.Salary_to, &rec_list.Requir, &rec_list.Respons, &rec_list.Url, 
			&rec_list.Company, &rec_list.Schedule, &rec_list.Vacancy_id, &rec_list.Adress, 
			&rec_list.Currency, &rec_list.Fk_telegram_id)
		if err != nil {
			panic(err)
			}
			Recs=append(Recs, rec_list)
		//  fmt.Println(rec_list.Records_id, rec_list.Vacancy_id)
	}
	return &Recs
}

func Get_one_record(vac_id string) *User_info{
	db := Db_connect()
	defer db.Close()
	records, err := db.Query(fmt.Sprintf("SELECT records_id,proff, vacancy, salary_from, salary_to, requir, respons, url, company, schedule, vacancy_id, adress, currency, fk_telegram_id FROM records inner join users  on users.telegram_id = records.fk_telegram_id WHERE vacancy_id='%s'", vac_id))
	if err != nil {
		panic(err)
	}
	Show_rec = User_info{}
	for records.Next(){
		var rec_list User_info
		err = records.Scan(&rec_list.Records_id,&rec_list.Proff, &rec_list.Vacancy, &rec_list.Salary_from, 
			&rec_list.Salary_to, &rec_list.Requir, &rec_list.Respons, &rec_list.Url, 
			&rec_list.Company, &rec_list.Schedule, &rec_list.Vacancy_id, &rec_list.Adress, 
			&rec_list.Currency, &rec_list.Fk_telegram_id) 
			if err != nil {
			panic(err)
			}
		Show_rec = rec_list
	}
	return &Show_rec
}