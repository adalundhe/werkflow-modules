from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dynamo_db_on_demand_throughput_override_model import DynamoDBOnDemandThroughputOverrideModel
from .dynamo_db_provisioned_throughput_override_model import DynamoDBProvisionedThroughputOverrideModel
from .dynamo_db_replica_global_secondary_index_description_model import DynamoDBReplicaGlobalSecondaryIndexDescriptionModel
from .dynamo_db_table_class_summary_model import DynamoDBTableClassSummaryModel
from .dynamo_db_table_warm_throughput_description_model import DynamoDBTableWarmThroughputDescriptionModel


class DynamoDBReplicaDescriptionModel(BaseModel):
    RegionName: StrictStr | None = None
    ReplicaStatus: StrictStr | None = None
    ReplicaArn: StrictStr | None = None
    ReplicaStatusDescription: StrictStr | None = None
    ReplicaStatusPercentProgress: StrictStr | None = None
    KMSMasterKeyId: StrictStr | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputOverrideModel | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputOverrideModel | None = None
    WarmThroughput: DynamoDBTableWarmThroughputDescriptionModel | None = None
    GlobalSecondaryIndexes: list[DynamoDBReplicaGlobalSecondaryIndexDescriptionModel] | None = None
    ReplicaInaccessibleDateTime: datetime.datetime | StrictStr | None = None
    ReplicaTableClassSummary: DynamoDBTableClassSummaryModel | None = None
    GlobalTableSettingsReplicationMode: StrictStr | None = None
