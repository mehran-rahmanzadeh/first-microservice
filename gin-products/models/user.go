package models

type User struct {
	ID         uint   `json:"id"`
	Username   string `json:"username"`
	Email      string `json:"email"`
	Lastname   string `json:"last_name"`
	Firstname  string `json:"first_name"`
	IsStaff    bool   `json:"is_staff"`
	IsActive   bool   `json:"is_active"`
	DateJoined string `json:"date_joined"`
	LastLogin  string `json:"last_login"`
}
