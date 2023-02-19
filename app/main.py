import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
