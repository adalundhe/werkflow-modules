from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_provisioned_throughput import DynamoDBProvisionedThroughput
from .dynamo_db_warm_throughput import DynamoDBWarmThroughput


class DynamoDBUpdateGlobalSecondaryIndexAction(BaseModel):
    IndexName: StrictStr
    ProvisionedThroughput: DynamoDBProvisionedThroughput | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    WarmThroughput: DynamoDBWarmThroughput | None = None
