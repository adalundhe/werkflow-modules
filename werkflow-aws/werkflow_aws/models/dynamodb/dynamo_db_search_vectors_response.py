from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dynamo_db_search_result_item import DynamoDBSearchResultItem
from .dynamo_db_vector_capacity_model import DynamoDBVectorCapacityModel


class DynamoDBSearchVectorsResponse(BaseModel):
    ConsumedCapacity: DynamoDBVectorCapacityModel | None = None
    SearchResults: list[DynamoDBSearchResultItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
