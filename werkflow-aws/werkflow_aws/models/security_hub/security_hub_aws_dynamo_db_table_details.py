from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_dynamo_db_table_attribute_definition import SecurityHubAwsDynamoDbTableAttributeDefinition
from .security_hub_aws_dynamo_db_table_billing_mode_summary import SecurityHubAwsDynamoDbTableBillingModeSummary
from .security_hub_aws_dynamo_db_table_global_secondary_index import SecurityHubAwsDynamoDbTableGlobalSecondaryIndex
from .security_hub_aws_dynamo_db_table_key_schema import SecurityHubAwsDynamoDbTableKeySchema
from .security_hub_aws_dynamo_db_table_local_secondary_index import SecurityHubAwsDynamoDbTableLocalSecondaryIndex
from .security_hub_aws_dynamo_db_table_provisioned_throughput import SecurityHubAwsDynamoDbTableProvisionedThroughput
from .security_hub_aws_dynamo_db_table_replica import SecurityHubAwsDynamoDbTableReplica
from .security_hub_aws_dynamo_db_table_restore_summary import SecurityHubAwsDynamoDbTableRestoreSummary
from .security_hub_aws_dynamo_db_table_sse_description import SecurityHubAwsDynamoDbTableSseDescription
from .security_hub_aws_dynamo_db_table_stream_specification import SecurityHubAwsDynamoDbTableStreamSpecification


class SecurityHubAwsDynamoDbTableDetails(BaseModel):
    AttributeDefinitions: list[SecurityHubAwsDynamoDbTableAttributeDefinition] | None = None
    BillingModeSummary: SecurityHubAwsDynamoDbTableBillingModeSummary | None = None
    CreationDateTime: StrictStr | None = None
    GlobalSecondaryIndexes: list[SecurityHubAwsDynamoDbTableGlobalSecondaryIndex] | None = None
    GlobalTableVersion: StrictStr | None = None
    ItemCount: StrictInt | None = None
    KeySchema: list[SecurityHubAwsDynamoDbTableKeySchema] | None = None
    LatestStreamArn: StrictStr | None = None
    LatestStreamLabel: StrictStr | None = None
    LocalSecondaryIndexes: list[SecurityHubAwsDynamoDbTableLocalSecondaryIndex] | None = None
    ProvisionedThroughput: SecurityHubAwsDynamoDbTableProvisionedThroughput | None = None
    Replicas: list[SecurityHubAwsDynamoDbTableReplica] | None = None
    RestoreSummary: SecurityHubAwsDynamoDbTableRestoreSummary | None = None
    SseDescription: SecurityHubAwsDynamoDbTableSseDescription | None = None
    StreamSpecification: SecurityHubAwsDynamoDbTableStreamSpecification | None = None
    TableId: StrictStr | None = None
    TableName: StrictStr | None = None
    TableSizeBytes: StrictInt | None = None
    TableStatus: StrictStr | None = None
    DeletionProtectionEnabled: StrictBool | None = None
