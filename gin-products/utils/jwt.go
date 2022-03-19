package utils

import (
	"gin-products/config"
	"gin-products/models"
	"github.com/go-resty/resty/v2"
	"net/http"
)

type VerifyTokenBody struct {
	Token string `json:"token"`
}

func ValidateToken(token string) (models.User, bool) {
	client := resty.New()
	response, _ := client.R().
		SetHeader("Content-Type", "application/json").
		SetBody(VerifyTokenBody{Token: token}).
		Post(config.Settings.Microservice.TokenVerifyEndpoint)
	if response.StatusCode() != http.StatusOK {
		return models.User{}, false
	}
	user := models.User{}
	response, _ = client.R().
		SetAuthToken(token).
		SetResult(&user).
		Get(config.Settings.Microservice.UserDetailEndpoint)
	return user, true
}
