
def get_postgres_uri(user, password, host, port, database):
    return f'postgresql://{user}:{password}@{host}:{port}/{database}'
