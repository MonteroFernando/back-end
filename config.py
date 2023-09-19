from dotenv import dotenv_values

class Config:
    config= dotenv_values(".env")

    SECRET_KEY=""
    SERVER_NAME=""
    DEBUG=True

    DATABASE_USER_NAME=""
    DATABASE_PASSWORD=""
    DATABASE_HOST=""
    DATABASE_PORT=""
    DATABASE_NAME=""
