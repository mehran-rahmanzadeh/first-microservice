package models

import "github.com/jinzhu/gorm"

type Category struct {
	gorm.Model
	Title    string    `json:"title" binding:"required"`
	Parent   *Category `json:"parent"`
	ParentID *int      `json:"parent_id"`
}

type CreateCategory struct {
	Title    string `json:"title" binding:"required"`
	ParentID *int   `json:"parent_id"`
}

type EditCategory struct {
	Title    string `json:"title"`
	ParentID *int   `json:"parent_id"`
}
