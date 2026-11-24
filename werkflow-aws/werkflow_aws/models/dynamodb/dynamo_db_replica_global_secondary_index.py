from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_on_demand_throughput_override import DynamoDBOnDemandThroughputOverride
from .dynamo_db_provisioned_throughput_override import DynamoDBProvisionedThroughputOverride


class DynamoDBReplicaGlobalSecondaryIndex(BaseModel):
    IndexName: StrictStr
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverride | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverride | None = None
