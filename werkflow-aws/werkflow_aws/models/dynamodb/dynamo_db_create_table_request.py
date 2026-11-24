from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_attribute_definition import DynamoDBAttributeDefinition
from .dynamo_db_billing_mode import DynamoDBBillingMode
from .dynamo_db_global_secondary_index import DynamoDBGlobalSecondaryIndex
from .dynamo_db_global_table_settings_replication_mode import DynamoDBGlobalTableSettingsReplicationMode
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_local_secondary_index import DynamoDBLocalSecondaryIndex
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_provisioned_throughput import DynamoDBProvisionedThroughput
from .dynamo_db_stream_specification import DynamoDBStreamSpecification
from .dynamo_db_table_class import DynamoDBTableClass
from .dynamo_db_tag import DynamoDBTag
from .dynamo_db_vector_index import DynamoDBVectorIndex
from .dynamo_db_warm_throughput import DynamoDBWarmThroughput
from .dynamo_dbsse_specification import DynamoDBSSESpecification


class DynamoDBCreateTableRequest(BaseModel):
    TableName: StrictStr
    AttributeDefinitions: list[DynamoDBAttributeDefinition] | None = None
    KeySchema: list[DynamoDBKeySchemaElement] | None = None
    LocalSecondaryIndexes: list[DynamoDBLocalSecondaryIndex] | None = None
    GlobalSecondaryIndexes: list[DynamoDBGlobalSecondaryIndex] | None = None
    BillingMode: DynamoDBBillingMode | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughput | None = None
    StreamSpecification: DynamoDBStreamSpecification | None = None
    SSESpecification: DynamoDBSSESpecification | None = None
    Tags: list[DynamoDBTag] | None = None
    TableClass: DynamoDBTableClass | None = None
    DeletionProtectionEnabled: StrictBool | None = None
    WarmThroughput: DynamoDBWarmThroughput | None = None
    ResourcePolicy: StrictStr | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    GlobalTableSourceArn: StrictStr | None = None
    GlobalTableSettingsReplicationMode: DynamoDBGlobalTableSettingsReplicationMode | None = None
    VectorIndexes: list[DynamoDBVectorIndex] | None = None
