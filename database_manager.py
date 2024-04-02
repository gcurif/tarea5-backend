from mongoengine import connect

def get_db():
    db = connect(
        db="pafcat-dev",
        host="monorail.proxy.rlwy.net",
        port=28844,
        username="mongo",
        password="XHjuvEIfatAllcolCJnZPRplvycBoVLA"
    )
    return db
