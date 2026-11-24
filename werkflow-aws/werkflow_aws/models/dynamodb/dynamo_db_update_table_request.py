from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_attribute_definition import DynamoDBAttributeDefinition
from .dynamo_db_billing_mode import DynamoDBBillingMode
from .dynamo_db_global_secondary_index_update import DynamoDBGlobalSecondaryIndexUpdate
from .dynamo_db_global_table_settings_replication_mode import DynamoDBGlobalTableSettingsReplicationMode
from .dynamo_db_global_table_witness_group_update import DynamoDBGlobalTableWitnessGroupUpdate
from .dynamo_db_multi_region_consistency import DynamoDBMultiRegionConsistency
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_provisioned_throughput import DynamoDBProvisionedThroughput
from .dynamo_db_replication_group_update import DynamoDBReplicationGroupUpdate
from .dynamo_db_stream_specification import DynamoDBStreamSpecification
from .dynamo_db_table_class import DynamoDBTableClass
from .dynamo_db_vector_index_update import DynamoDBVectorIndexUpdate
from .dynamo_db_warm_throughput import DynamoDBWarmThroughput
from .dynamo_dbsse_specification import DynamoDBSSESpecification


class DynamoDBUpdateTableRequest(BaseModel):
    TableName: StrictStr
    AttributeDefinitions: list[DynamoDBAttributeDefinition] | None = None
    BillingMode: DynamoDBBillingMode | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughput | None = None
    GlobalSecondaryIndexUpdates: list[DynamoDBGlobalSecondaryIndexUpdate] | None = None
    StreamSpecification: DynamoDBStreamSpecification | None = None
    SSESpecification: DynamoDBSSESpecification | None = None
    ReplicaUpdates: list[DynamoDBReplicationGroupUpdate] | None = None
    TableClass: DynamoDBTableClass | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    MultiRegionConsistency: DynamoDBMultiRegionConsistency | None = None
    GlobalTableWitnessUpdates: list[DynamoDBGlobalTableWitnessGroupUpdate] | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    WarmThroughput: DynamoDBWarmThroughput | None = None
    GlobalTableSettingsReplicationMode: DynamoDBGlobalTableSettingsReplicationMode | None = None
    DisassociationProtectionEnabled: StrictBool | None = None
    VectorIndexUpdates: list[DynamoDBVectorIndexUpdate] | None = None
