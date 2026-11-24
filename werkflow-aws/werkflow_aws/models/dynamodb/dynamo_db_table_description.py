from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_archival_summary import DynamoDBArchivalSummary
from .dynamo_db_attribute_definition import DynamoDBAttributeDefinition
from .dynamo_db_billing_mode_summary import DynamoDBBillingModeSummary
from .dynamo_db_global_secondary_index_description import DynamoDBGlobalSecondaryIndexDescription
from .dynamo_db_global_table_settings_replication_mode import DynamoDBGlobalTableSettingsReplicationMode
from .dynamo_db_global_table_witness_description import DynamoDBGlobalTableWitnessDescription
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_local_secondary_index_description import DynamoDBLocalSecondaryIndexDescription
from .dynamo_db_multi_region_consistency import DynamoDBMultiRegionConsistency
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_provisioned_throughput_description import DynamoDBProvisionedThroughputDescription
from .dynamo_db_replica_description import DynamoDBReplicaDescription
from .dynamo_db_restore_summary import DynamoDBRestoreSummary
from .dynamo_db_stream_specification import DynamoDBStreamSpecification
from .dynamo_db_table_class_summary import DynamoDBTableClassSummary
from .dynamo_db_table_status import DynamoDBTableStatus
from .dynamo_db_table_warm_throughput_description import DynamoDBTableWarmThroughputDescription
from .dynamo_db_vector_index_description import DynamoDBVectorIndexDescription
from .dynamo_dbsse_description import DynamoDBSSEDescription


class DynamoDBTableDescription(BaseModel):
    AttributeDefinitions: list[DynamoDBAttributeDefinition] | None = None
    TableName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElement] | None = None
    TableStatus: DynamoDBTableStatus | None = None
    CreationDateTime: datetime.datetime | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputDescription | None = None
    TableSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    TableArn: StrictStr | None = None
    TableId: StrictStr | None = None
    BillingModeSummary: DynamoDBBillingModeSummary | None = None
    LocalSecondaryIndexes: list[DynamoDBLocalSecondaryIndexDescription] | None = None
    GlobalSecondaryIndexes: list[DynamoDBGlobalSecondaryIndexDescription] | None = None
    StreamSpecification: DynamoDBStreamSpecification | None = None
    LatestStreamLabel: StrictStr | None = None
    LatestStreamArn: StrictStr | None = None
    GlobalTableVersion: StrictStr | None = None
    Replicas: list[DynamoDBReplicaDescription] | None = None
    GlobalTableWitnesses: list[DynamoDBGlobalTableWitnessDescription] | None = None
    GlobalTableSettingsReplicationMode: DynamoDBGlobalTableSettingsReplicationMode | None = None
    RestoreSummary: DynamoDBRestoreSummary | None = None
    SSEDescription: DynamoDBSSEDescription | None = None
    ArchivalSummary: DynamoDBArchivalSummary | None = None
    TableClassSummary: DynamoDBTableClassSummary | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    DisassociationProtectionEnabled: StrictBool | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    WarmThroughput: DynamoDBTableWarmThroughputDescription | None = None
    MultiRegionConsistency: DynamoDBMultiRegionConsistency | None = None
    VectorIndexes: list[DynamoDBVectorIndexDescription] | None = None
