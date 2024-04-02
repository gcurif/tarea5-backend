from mongoengine import connect

def get_db():
    db = connect(
        db="pafcat-{aqui_tu_usuario}",
        host="monorail.proxy.rlwy.net",
        port=28844,
        username="mongo",
        password="XHjuvEIfatAllcolCJnZPRplvycBoVLA"
    )
    return db
