package models

import "github.com/jinzhu/gorm"

type Product struct {
	gorm.Model
	Title              string   `json:"title"`
	Slug               string   `json:"slug" gorm:"unique"`
	Description        string   `json:"description"`
	Price              float64  `json:"price"`
	PriceAfterDiscount float64  `json:"price_after_discount"`
	HasDiscount        bool     `json:"has_discount" gorm:"default:false"`
	Category           Category `json:"category"`
	CategoryID         int      `json:"category_id"`
}

type CreateProduct struct {
	Title              string  `json:"title"`
	Slug               string  `json:"slug" gorm:"unique"`
	Description        string  `json:"description"`
	Price              float64 `json:"price"`
	PriceAfterDiscount float64 `json:"price_after_discount"`
	HasDiscount        bool    `json:"has_discount" gorm:"default:false"`
	CategoryID         int     `json:"category_id"`
}

type EditProduct struct {
	Title              string  `json:"title"`
	Slug               string  `json:"slug" gorm:"unique"`
	Description        string  `json:"description"`
	Price              float64 `json:"price"`
	PriceAfterDiscount float64 `json:"price_after_discount"`
	HasDiscount        bool    `json:"has_discount" gorm:"default:false"`
	CategoryID         int     `json:"category_id"`
}

type ProductFilter struct {
	Title              string  `form:"title"`
	Slug               string  `form:"slug"`
	Description        string  `form:"description"`
	Price              float64 `form:"price"`
	PriceAfterDiscount float64 `form:"price_after_discount"`
	HasDiscount        bool    `form:"has_discount"`
	CategoryID         int     `form:"category_id"`
}

type ProductSearch struct {
	Query string `form:"q"`
}
