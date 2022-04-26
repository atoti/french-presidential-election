import atoti as tt


def create_users(session: tt.Session, /) -> None:
    elon = session.security.basic.create_user("user", password="user")
    session.security.individual_roles[elon.username].add("ROLE_USER")
    print(f"User created with roles: {elon.roles}")

    admin = session.security.basic.create_user("tt_admin", password="tt_admin")
    session.security.individual_roles[admin.username].add("ROLE_ADMIN")
    session.security.individual_roles[admin.username].add("ROLE_SHARE")
    print(f"Admin created with roles: {admin.roles}")
