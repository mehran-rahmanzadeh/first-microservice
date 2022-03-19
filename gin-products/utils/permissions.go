package utils

import (
	"github.com/gin-gonic/gin"
	"github.com/oleiade/reflections"
)

func IsAdmin(c *gin.Context) bool {
	var user = c.MustGet("user")
	value, _ := reflections.GetField(user, "IsStaff")
	return value.(bool)
}
