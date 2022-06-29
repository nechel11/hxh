package pages

import (
	"fmt"
	"html/template"
	"net/http"
	_ "github.com/lib/pq"
	"database/sql"
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


func show_vac_list(username string){
	psqconn := fmt.Sprintf("host= %s port = %d user = %s password = %s dbname = %s sslmode=disable", host, port, user, password, dbname)
	db, _ := sql.Open("postgres", psqconn)
	defer db.Close()

}