from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_dynamo_db_capacity_details import CostExplorerDynamoDBCapacityDetails


class CostExplorerReservedCapacityDetails(BaseModel):
    DynamoDBCapacityDetails: CostExplorerDynamoDBCapacityDetails | None = None
