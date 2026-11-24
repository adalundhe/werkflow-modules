from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_dynamo_db_table_provisioned_throughput_override import SecurityHubAwsDynamoDbTableProvisionedThroughputOverride
from .security_hub_aws_dynamo_db_table_replica_global_secondary_index import SecurityHubAwsDynamoDbTableReplicaGlobalSecondaryIndex


class SecurityHubAwsDynamoDbTableReplica(BaseModel):
    GlobalSecondaryIndexes: list[SecurityHubAwsDynamoDbTableReplicaGlobalSecondaryIndex] | None = None
    KmsMasterKeyId: StrictStr | None = None
    ProvisionedThroughputOverride: SecurityHubAwsDynamoDbTableProvisionedThroughputOverride | None = None
    RegionName: StrictStr | None = None
    ReplicaStatus: StrictStr | None = None
    ReplicaStatusDescription: StrictStr | None = None
