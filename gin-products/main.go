package main

import (
	"gin-products/config"
	"gin-products/controllers"
	"gin-products/middlewares"
	"gin-products/models"
	"github.com/gin-gonic/gin"
)

var router *gin.Engine

func main() {
	// initiate default router
	router = gin.Default()
	group := router.Group("/api/v1/")
	privateGroup := router.Group("/api/v1/")
	privateGroup.Use(middlewares.AuthorizeJWT())

	// initialize config file
	config.InitializeConfig()

	// connect to db
	models.ConnectDatabase()

	// Public API Endpoints
	group.GET("categories/", controllers.CategoryList)
	group.GET("categories/:id/", controllers.CategoryDetail)
	group.GET("products/", controllers.ProductList)
	group.GET("products/:id/", controllers.ProductDetail)

	// Private API Endpoints
	privateGroup.POST("categories/", controllers.CreateCategory)
	privateGroup.PATCH("categories/:id/", controllers.EditCategory)
	privateGroup.POST("products/", controllers.CreateProduct)
	privateGroup.PATCH("products/:id/", controllers.EditProduct)

	// start serving the application
	err := router.Run(config.Settings.Server.Port)
	if err != nil {
		return
	}
}
