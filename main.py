from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables
from router import router as task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database droped")
    await create_tables()
    print("Database created")
    yield
    print("End")

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)







