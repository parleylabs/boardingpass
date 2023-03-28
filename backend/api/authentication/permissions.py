# Permission specifications based on Gare du Nord - User Roles requirement doc:
# https://docs.google.com/spreadsheets/d/1pc6nSuKAWRwdNhLUqQxB0nIdjO4U-Y1YxTjcFKAw6l4/edit#gid=0

def can_view_all_keys(user):
    return user.is_active and user.is_admin