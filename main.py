from fastapi import FastAPI
from api import users, sections, courses


app = FastAPI()

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)




if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8003 )