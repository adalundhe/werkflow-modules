from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_create_vector_index_action import DynamoDBCreateVectorIndexAction
from .dynamo_db_delete_vector_index_action import DynamoDBDeleteVectorIndexAction


class DynamoDBVectorIndexUpdate(BaseModel):
    Create: DynamoDBCreateVectorIndexAction | None = None
    Delete: DynamoDBDeleteVectorIndexAction | None = None
