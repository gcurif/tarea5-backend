from mongoengine import connect

def get_db():
    db = connect(
        db="pafcat-static",
        host="viaduct.proxy.rlwy.net",
        port=28844,
        username="leinas",
        password="pafcat.2024"
    )
    return db
