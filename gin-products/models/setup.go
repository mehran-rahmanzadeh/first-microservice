package models

import (
	"fmt"
	"gin-products/config"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *gorm.DB

func ConnectDatabase() {
	dbURL := fmt.Sprintf(
		"postgres://%s:%s@%s:%s/%s",
		config.Settings.Database.DBUser,
		config.Settings.Database.DBPassword,
		config.Settings.Database.DBHost,
		config.Settings.Database.DBPort,
		config.Settings.Database.DBName,
	)
	database, err := gorm.Open(postgres.Open(dbURL), &gorm.Config{})

	if err != nil {
		panic("Failed to connect to database!")
	}

	migrateCategoryErr := database.AutoMigrate(&Category{})
	if migrateCategoryErr != nil {
		panic(migrateCategoryErr)
	}
	migrateProductErr := database.AutoMigrate(&Product{})
	if migrateProductErr != nil {
		panic(migrateProductErr)
	}

	DB = database
}
