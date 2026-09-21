package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// import "github.com/joho/godotenv"
// if err := godotenv.Load(); err != nil { log.Println("No .env file found") }

func main() {
	// uri := os.Getenv("MONGODB_URI")
	// "C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="E:\mgo\test"
	uri := "mongodb://localhost:27017/?retryWrites=true&w=majority"
	if uri == "" {
		log.Fatal("Set your 'MONGODB_URI' environment variable. " +
			"See: " +
			"www.mongodb.com/docs/drivers/go/current/usage-examples/#environment-variable")
	}
	client, err := mongo.Connect(context.TODO(), options.Client().
		ApplyURI(uri))
	if err != nil {
		panic(err)
	}

	defer func() {
		if err := client.Disconnect(context.TODO()); err != nil {
			panic(err)
		}
	}()

	coll := client.Database("test").Collection("testc")
	title := "https://twitter.com/"

	var result bson.M
	// err = coll.FindOne(context.TODO(), bson.D{{"url", title}}).Decode(&result)
	opts := options.Count().SetHint("_id_")
	count, err := coll.CountDocuments(context.TODO(), bson.D{}, opts)
	if err == mongo.ErrNoDocuments {
		fmt.Printf("No document was found with the title %s\n", title)
		return
	}
	if err != nil {
		panic(err)
	}
	fmt.Printf("%d\n", count)

	jsonData, err := json.MarshalIndent(result, "", "    ")
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s\n", jsonData)
}
