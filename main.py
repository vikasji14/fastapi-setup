from fastapi import FastAPI
from api import users, sections, courses


app = FastAPI(
    title="Faraday API",
    description="API for Faraday",
    version="1.0.0",
    contact={"name": "vikas Team", "email": "vikas@gmail.com"}


)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)




if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8003 )