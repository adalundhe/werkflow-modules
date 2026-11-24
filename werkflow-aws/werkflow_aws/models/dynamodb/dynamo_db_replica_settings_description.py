from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_description import DynamoDBAutoScalingSettingsDescription
from .dynamo_db_billing_mode_summary_model import DynamoDBBillingModeSummaryModel
from .dynamo_db_replica_global_secondary_index_settings_description import DynamoDBReplicaGlobalSecondaryIndexSettingsDescription
from .dynamo_db_table_class_summary_model import DynamoDBTableClassSummaryModel


class DynamoDBReplicaSettingsDescription(BaseModel):
    RegionName: StrictStr | None = None
    ReplicaStatus: StrictStr | None = None
    ReplicaBillingModeSummary: DynamoDBBillingModeSummaryModel | None = None
    ReplicaProvisionedReadCapacityUnits: StrictInt | None = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ReplicaProvisionedWriteCapacityUnits: StrictInt | None = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: DynamoDBAutoScalingSettingsDescription | None = None
    ReplicaGlobalSecondaryIndexSettings: list[DynamoDBReplicaGlobalSecondaryIndexSettingsDescription] | None = None
    ReplicaTableClassSummary: DynamoDBTableClassSummaryModel | None = None
