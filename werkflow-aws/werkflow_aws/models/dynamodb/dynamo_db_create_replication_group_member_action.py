from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_on_demand_throughput_override import DynamoDBOnDemandThroughputOverride
from .dynamo_db_provisioned_throughput_override import DynamoDBProvisionedThroughputOverride
from .dynamo_db_replica_global_secondary_index import DynamoDBReplicaGlobalSecondaryIndex
from .dynamo_db_table_class import DynamoDBTableClass


class DynamoDBCreateReplicationGroupMemberAction(BaseModel):
    RegionName: StrictStr
    KMSMasterKeyId: StrictStr | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverride | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverride | None = None
    GlobalSecondaryIndexes: list[DynamoDBReplicaGlobalSecondaryIndex] | None = None
    TableClassOverride: DynamoDBTableClass | None = None
