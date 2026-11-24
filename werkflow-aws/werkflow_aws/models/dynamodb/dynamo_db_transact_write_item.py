from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_condition_check import DynamoDBConditionCheck
from .dynamo_db_delete import DynamoDBDelete
from .dynamo_db_put import DynamoDBPut
from .dynamo_db_update import DynamoDBUpdate


class DynamoDBTransactWriteItem(BaseModel):
    ConditionCheck: DynamoDBConditionCheck | None = None
    Put: DynamoDBPut | None = None
    Delete: DynamoDBDelete | None = None
    Update: DynamoDBUpdate | None = None
