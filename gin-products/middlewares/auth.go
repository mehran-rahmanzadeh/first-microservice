package middlewares

import (
	"gin-products/utils"
	"net/http"

	"github.com/gin-gonic/gin"
)

func AuthorizeJWT() gin.HandlerFunc {
	return func(c *gin.Context) {
		const BearerSchema = "Bearer "
		authHeader := c.GetHeader("Authorization")
		if len(authHeader) > 0 {
			tokenString := authHeader[len(BearerSchema):]
			user, isValid := utils.ValidateToken(tokenString)
			if isValid {
				c.Set("user", user)
			} else {
				c.AbortWithStatus(http.StatusUnauthorized)
			}
		} else {
			c.AbortWithStatus(http.StatusUnauthorized)
		}
	}
}
