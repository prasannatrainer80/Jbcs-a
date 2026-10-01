class Config:

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:root@localhost:3306/studentdb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False