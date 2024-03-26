from services.user import UserService
from services.user_dog import UserDogService
from db.database import users, dogs

users = UserService(users)
users_dogs = UserDogService(dogs)

