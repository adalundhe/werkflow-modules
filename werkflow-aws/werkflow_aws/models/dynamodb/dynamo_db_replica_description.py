from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dynamo_db_global_table_settings_replication_mode import DynamoDBGlobalTableSettingsReplicationMode
from .dynamo_db_on_demand_throughput_override import DynamoDBOnDemandThroughputOverride
from .dynamo_db_provisioned_throughput_override import DynamoDBProvisionedThroughputOverride
from .dynamo_db_replica_global_secondary_index_description import DynamoDBReplicaGlobalSecondaryIndexDescription
from .dynamo_db_replica_status import DynamoDBReplicaStatus
from .dynamo_db_table_class_summary import DynamoDBTableClassSummary
from .dynamo_db_table_warm_throughput_description import DynamoDBTableWarmThroughputDescription


class DynamoDBReplicaDescription(BaseModel):
    RegionName: StrictStr | None = None
    ReplicaStatus: DynamoDBReplicaStatus | None = None
    ReplicaArn: StrictStr | None = None
    ReplicaStatusDescription: StrictStr | None = None
    ReplicaStatusPercentProgress: StrictStr | None = None
    KMSMasterKeyId: StrictStr | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverride | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverride | None = None
    WarmThroughput: DynamoDBTableWarmThroughputDescription | None = None
    GlobalSecondaryIndexes: list[DynamoDBReplicaGlobalSecondaryIndexDescription] | None = None
    ReplicaInaccessibleDateTime: datetime.datetime | None = None
    ReplicaTableClassSummary: DynamoDBTableClassSummary | None = None
    GlobalTableSettingsReplicationMode: DynamoDBGlobalTableSettingsReplicationMode | None = None
