from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_create_global_secondary_index_action import DynamoDBCreateGlobalSecondaryIndexAction
from .dynamo_db_delete_global_secondary_index_action import DynamoDBDeleteGlobalSecondaryIndexAction
from .dynamo_db_update_global_secondary_index_action import DynamoDBUpdateGlobalSecondaryIndexAction


class DynamoDBGlobalSecondaryIndexUpdate(BaseModel):
    Update: DynamoDBUpdateGlobalSecondaryIndexAction | None = None
    Create: DynamoDBCreateGlobalSecondaryIndexAction | None = None
    Delete: DynamoDBDeleteGlobalSecondaryIndexAction | None = None
