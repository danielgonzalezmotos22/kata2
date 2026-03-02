import jwt
from fastapi import HTTPException, request

SECRET_KEY = "supersecret"
app = Fastapi()

@app.middleware("http")
async def jwt_auth_middleware(request: Request, call_next):

    if request.url.path.startswith("/private"):
        token = request.headers.get("Authorization")

        if not token:
            raise HTTPException(status_code=401, detail="Token requerido")

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.state.user = payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token inválido")

    response = await call_next(request)
    return response