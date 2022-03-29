package controllers

import (
	"gin-products/models"
	"gin-products/utils"
	"net/http"

	"github.com/gin-gonic/gin"
)

func ProductList(c *gin.Context) {
	var products []models.Product
	var filters models.ProductFilter
	var search models.ProductSearch
	if err := c.ShouldBind(&filters); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": "Bad query params"})
		return
	}
	if err := c.ShouldBind(&search); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": "Bad query params"})
		return
	}
	models.DB.Where(filters).Where(
		"title iLIKE ?", "%"+search.Query+"%").Preload(
		"Category").Find(&products)

	c.JSON(http.StatusOK, gin.H{"result": products})
}

func ProductDetail(c *gin.Context) {
	var product models.Product
	if err := models.DB.Where("id = ?", c.Param("id")).Preload("Category").First(&product).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"message": "Product not found."})
		return
	}

	c.JSON(http.StatusOK, gin.H{"result": product})
}

func CreateProduct(c *gin.Context) {
	if !utils.IsAdmin(c) {
		c.JSON(http.StatusForbidden, gin.H{"message": "Permission denied"})
		return
	}
	var input models.CreateProduct
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}

	var product models.Product = models.Product{
		Title:              input.Title,
		Slug:               input.Slug,
		Description:        input.Description,
		Price:              input.Price,
		PriceAfterDiscount: input.PriceAfterDiscount,
		HasDiscount:        input.HasDiscount,
		CategoryID:         input.CategoryID,
	}
	models.DB.Create(&product)
	c.JSON(http.StatusCreated, gin.H{"result": product})
}

func EditProduct(c *gin.Context) {
	if !utils.IsAdmin(c) {
		c.JSON(http.StatusForbidden, gin.H{"message": "Permission denied"})
		return
	}
	var product models.Product
	if err := models.DB.Where("id = ?", c.Param("id")).First(&product).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"message": "Product not found"})
		return
	}

	var input models.EditProduct
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
		return
	}
	models.DB.Model(&product).Updates(input)
	c.JSON(http.StatusAccepted, gin.H{"result": product})
}
