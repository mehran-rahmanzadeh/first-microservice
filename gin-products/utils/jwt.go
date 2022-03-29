package utils

import (
	"context"
	"gin-products/config"
	"gin-products/models"
	pb "gin-products/proto"

	"github.com/go-resty/resty/v2"
	"google.golang.org/grpc"
)

type VerifyTokenBody struct {
	Token string `json:"token"`
}

func ValidateToken(token string) (models.User, bool) {

	// connect to gRPC server
	conn, err := grpc.Dial(config.Settings.Microservice.GRPC, grpc.WithInsecure())
	if err != nil {
		panic("Cannot connect to gRPC server")
	}
	defer conn.Close()

	isAuthenticated := false

	// call verify token method in gRPC proto
	grpcClient := pb.NewAuthControllerClient(conn)
	grpcResp, err := grpcClient.VerifyToken(context.Background(), &pb.VerifyRequest{Token: token})
	if err != nil {
		isAuthenticated = false
		return models.User{}, false
	}

	isAuthenticated = grpcResp.Access

	// get user detail using http
	if isAuthenticated {
		client := resty.New()
		user := models.User{}
		client.R().
			SetAuthToken(token).
			SetResult(&user).
			Get(config.Settings.Microservice.UserDetailEndpoint)
		return user, true
	} else {
		return models.User{}, false
	}

}
