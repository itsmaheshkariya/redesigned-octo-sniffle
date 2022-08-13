import graphene
class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    password = graphene.String()