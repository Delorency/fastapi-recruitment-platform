from sqladmin import ModelView

from app.main import admin
from app.model.user_model import User



class UserAdminView(ModelView, model=User):
	category = "Accounts"
	name_plural = "Users"
	name = "User"
	icon = "fa-solid fa-user"

	column_list = ['id', 'username', 'email', 'name', 
					'password', 'created_at', 'updated_at']

	column_searchable_list = ['id', 'email', 'username','name']
	column_sortable_list = ['email']



admin.add_view(UserAdminView)