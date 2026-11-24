from __future__ import annotations
import datetime
from pydantic import BaseModel
from .dynamo_db_table_class import DynamoDBTableClass


class DynamoDBTableClassSummary(BaseModel):
    TableClass: DynamoDBTableClass | None = None
    LastUpdateDateTime: datetime.datetime | None = None
