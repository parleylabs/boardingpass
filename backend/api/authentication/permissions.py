
def can_create_superuser(user):
    return user.is_superuser


def can_create_user_in_org(user, organization):
    if user.is_superuser:
        return True

    if user.is_staff and (user.organization == organization):
        return True

    return False
