package models

type user struct {
	Username string `bson:"Username" json:"Username"`
	Email string `bson:"Email" json:"Email"`
	Password string `bson:"Password" json:"Password"`
}
