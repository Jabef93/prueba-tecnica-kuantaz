from decouple import config
from app.utils import get_postgres_uri


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_postgres_uri(
        host=config('PGSQL_HOST'),
        port=config('PGSQL_PORT'),
        user=config('PGSQL_USER'),
        password=config('PGSQL_PASSWORD'),
        database=config('PGSQL_DATABASE')
    )


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
