
def can_view_all_keys(user):
    return user.is_active and user.is_admin