func Get<%modelName%>(filter bson.M) (*<%modelName%>, error) {
	db, err := database.GetMongoDB()
	if err != nil {
		return nil, err
	}
	col := db.Collection(<%collection%>)

	res := col.FindOne(context.TODO(), filter)
	if res.Err() != nil {
		return nil, res.Err()
	}

	var s models.<%modelName%>
	err = res.Decode(&s)
	if err != nil {
		return nil, err
	}

	return &s, nil
}