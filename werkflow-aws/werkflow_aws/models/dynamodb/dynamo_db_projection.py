from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_projection_type import DynamoDBProjectionType


class DynamoDBProjection(BaseModel):
    ProjectionType: DynamoDBProjectionType | None = None
    NonKeyAttributes: list[StrictStr] | None = None
