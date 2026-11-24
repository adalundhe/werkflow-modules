from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_global_secondary_index_warm_throughput_description_model import DynamoDBGlobalSecondaryIndexWarmThroughputDescriptionModel
from .dynamo_db_on_demand_throughput_override_model import DynamoDBOnDemandThroughputOverrideModel
from .dynamo_db_provisioned_throughput_override_model import DynamoDBProvisionedThroughputOverrideModel


class DynamoDBReplicaGlobalSecondaryIndexDescriptionModel(BaseModel):
    IndexName: StrictStr | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverrideModel | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverrideModel | None = None
    WarmThroughput: DynamoDBGlobalSecondaryIndexWarmThroughputDescriptionModel | None = None
