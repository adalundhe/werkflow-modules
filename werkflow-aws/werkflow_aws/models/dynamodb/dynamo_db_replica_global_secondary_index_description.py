from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_global_secondary_index_warm_throughput_description import DynamoDBGlobalSecondaryIndexWarmThroughputDescription
from .dynamo_db_on_demand_throughput_override import DynamoDBOnDemandThroughputOverride
from .dynamo_db_provisioned_throughput_override import DynamoDBProvisionedThroughputOverride


class DynamoDBReplicaGlobalSecondaryIndexDescription(BaseModel):
    IndexName: StrictStr | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverride | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverride | None = None
    WarmThroughput: DynamoDBGlobalSecondaryIndexWarmThroughputDescription | None = None
