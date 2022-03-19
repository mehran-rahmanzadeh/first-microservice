package config

import (
	"github.com/spf13/viper"
)

type Config struct {
	Server       ServerConfig
	Database     DatabaseConfig
	Microservice MicroserviceConfig
}

type DatabaseConfig struct {
	DBHost     string
	DBUser     string
	DBPassword string
	DBPort     string
	DBName     string
}

type MicroserviceConfig struct {
	TokenVerifyEndpoint string
	UserDetailEndpoint  string
}

type ServerConfig struct {
	Port string
}

var Settings Config

func InitializeConfig() {
	viper.SetConfigName("config")
	viper.AddConfigPath(".")
	viper.AutomaticEnv()
	viper.SetConfigType("yml")

	var configuration Config
	if err := viper.ReadInConfig(); err != nil {
		panic("Error reading config file")
	}

	err := viper.Unmarshal(&configuration)
	if err != nil {
		panic("Unable to decode into struct")
	}
	Settings = configuration
}
