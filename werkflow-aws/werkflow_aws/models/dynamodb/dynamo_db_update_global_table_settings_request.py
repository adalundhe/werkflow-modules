from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_auto_scaling_settings_update import DynamoDBAutoScalingSettingsUpdate
from .dynamo_db_global_table_global_secondary_index_settings_update import DynamoDBGlobalTableGlobalSecondaryIndexSettingsUpdate
from .dynamo_db_replica_settings_update import DynamoDBReplicaSettingsUpdate


class DynamoDBUpdateGlobalTableSettingsRequest(BaseModel):
    GlobalTableName: StrictStr
    GlobalTableBillingMode: Literal['PROVISIONED', 'PAY_PER_REQUEST'] | None = None
    GlobalTableProvisionedWriteCapacityUnits: StrictInt | None = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: DynamoDBAutoScalingSettingsUpdate | None = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: list[DynamoDBGlobalTableGlobalSecondaryIndexSettingsUpdate] | None = None
    ReplicaSettingsUpdate: list[DynamoDBReplicaSettingsUpdate] | None = None
