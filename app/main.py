import strawberry
import asyncpg
import aiosql

from os import environ
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

db_name = environ["DB_NAME"]
db_user = environ["DB_USER"]
db_password = environ["DB_PASSWORD"]
db_host = environ["DB_HOST"]
db_port = environ["DB_PORT"]

db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

@app.get("/")
async def root():
    queries = aiosql.from_path("app/queries.sql", "asyncpg")
    # Making a connection to the postgresql database with the asyncpg driver
    connection = await asyncpg.connect(db_url)
    controls = await queries.get_all_controls(connection)
    return {"controls": controls}


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
