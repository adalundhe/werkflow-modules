from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_table_auto_scaling_description import DynamoDBTableAutoScalingDescription


class DynamoDBUpdateTableReplicaAutoScalingResponse(BaseModel):
    TableAutoScalingDescription: DynamoDBTableAutoScalingDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
