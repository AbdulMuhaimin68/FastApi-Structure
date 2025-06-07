from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:smartforum123@localhost/testdb"
    JWT_SECRET_KEY: str = "khanmuhaimin"

settings = Settings()
