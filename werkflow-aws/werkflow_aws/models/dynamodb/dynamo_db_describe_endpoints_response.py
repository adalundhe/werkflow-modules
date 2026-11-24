from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_endpoint import DynamoDBEndpoint


class DynamoDBDescribeEndpointsResponse(BaseModel):
    Endpoints: list[DynamoDBEndpoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
