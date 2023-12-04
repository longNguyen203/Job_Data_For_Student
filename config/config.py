class Config:
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql://postgres:@@LONG2003@localhost:5432/postgres'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'postgresql://postgres:@@LONG2003@localhost:5432/postgres'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'postgresql://postgres:@@LONG2003@localhost:5432/postgres'

def get_database_config() -> dict:
    # Hàm này trả về cấu hình cơ sở dữ liệu tùy thuộc vào môi trường
    if Config.DEBUG:
        return {'database_uri': DevelopmentConfig.DATABASE_URI}
    elif Config.TESTING:
        return {'database_uri': TestingConfig.DATABASE_URI}
    else:
        return {'database_uri': ProductionConfig.DATABASE_URI}