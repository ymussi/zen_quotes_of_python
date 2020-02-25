import graphene

class User(graphene.ObjectType):
    name = graphene.String()
    age = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):

    user = graphene.Field(User,)

    def resolve_user(self, info):
        return User(name="Yuri Mussi", age="27", email="ymussi@gmail.com")


schema =graphene.Schema(query=Query)
