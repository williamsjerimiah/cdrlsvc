""""Create configuration file for use within the application"""
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class to import environment variables"""
    arango_root_password: str
    arango_root_user: str
    arango_host: str
    arango_db: str
    database_hostname: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    minio_root_user: str
    minio_root_password: str
    minio_api_port: str
    minio_ui_port: str
    minio_s3_access_key: str
    minio_s3_secret_access_key: str
    server_url: str

    class Config:
        """Config to use .env variables"""
        env_file = '.env'


settings = Settings()

# @lru_cache()
# def get_setting():
#    return Settings()
# print(Settings().arango_root_password)
