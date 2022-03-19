package controllers

import (
	"gin-products/models"
	"gin-products/utils"
	"github.com/gin-gonic/gin"
	"net/http"
)

func CategoryList(c *gin.Context) {
	var categories []models.Category
	models.DB.Preload("Parent").Find(&categories)

	c.JSON(http.StatusOK, gin.H{"result": categories})
}

func CategoryDetail(c *gin.Context) {
	var category models.Category
	if err := models.DB.Where("id = ?", c.Param("id")).Preload("Parent").First(&category).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"message": "Category not found."})
	}

	c.JSON(http.StatusOK, gin.H{"result": category})
}

func CreateCategory(c *gin.Context) {
	if !utils.IsAdmin(c) {
		c.JSON(http.StatusForbidden, gin.H{"message": "Permission denied"})
		return
	}
	var input models.CreateCategory
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
	}

	var category models.Category = models.Category{Title: input.Title, ParentID: input.ParentID}
	models.DB.Create(&category)

	c.JSON(http.StatusCreated, gin.H{"result": category})
}

func EditCategory(c *gin.Context) {
	if !utils.IsAdmin(c) {
		c.JSON(http.StatusForbidden, gin.H{"message": "Permission denied"})
		return
	}
	var category models.Category
	if err := models.DB.Where("id = ?", c.Param("id")).First(&category).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"message": "Category not found."})
	}

	var input models.EditCategory
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"message": err.Error()})
	}

	models.DB.Model(&category).Updates(input)
	c.JSON(http.StatusAccepted, gin.H{"result": category})
}
