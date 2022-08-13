import graphene
from mutation import CreateUser, DeleteUser, UpdateUser
from query import Query
from graphene import String, ObjectType, Field, List

from type import User

class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()

class MyQuery(Query):
    user = Field(User)
    get_user = Field(User,id=String())
    get_users = List(User)

schema = graphene.Schema(query=MyQuery, mutation=MyMutations)
# result = schema.execute(
#     '''
#     mutation {
#         createUser(id: "2", name: "Mahesh", email: "mahesh@gmail.com", password: "123456") {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )
# print(result.data)




# result = schema.execute(
#     '''
#     mutation {
#         deleteUser(id: "1") {
#             user {
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     '''
# )
# print(result.data)

# query_string = '''
# { getUsers {
#     id
#     name
#     email
#     password
# } }'''
# result = schema.execute(query_string)
# print(result.data)



result = schema.execute(
    '''
    mutation {
        updateUser(id: "1", name: "MaheshK", email: "maheshK@gmail.com", password: "1234567") {
            user {
                id
                name
                email
                password
            }
        }
    }
    '''
)
print(result.data)

# query_string = '''
# { getUser(id: "1"){
#     id
#     name
#     email
#     password
# } }'''
# result = schema.execute(query_string)
# print(result.data)