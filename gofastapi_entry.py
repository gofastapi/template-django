from mangum import Mangum
from app.asgi import application as app

handler = Mangum(app, lifespan="off")
