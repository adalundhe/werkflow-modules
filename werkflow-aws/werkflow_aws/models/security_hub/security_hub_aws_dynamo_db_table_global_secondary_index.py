from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_dynamo_db_table_key_schema import SecurityHubAwsDynamoDbTableKeySchema
from .security_hub_aws_dynamo_db_table_projection import SecurityHubAwsDynamoDbTableProjection
from .security_hub_aws_dynamo_db_table_provisioned_throughput import SecurityHubAwsDynamoDbTableProvisionedThroughput


class SecurityHubAwsDynamoDbTableGlobalSecondaryIndex(BaseModel):
    Backfilling: StrictBool | None = None
    IndexArn: StrictStr | None = None
    IndexName: StrictStr | None = None
    IndexSizeBytes: StrictInt | None = None
    IndexStatus: StrictStr | None = None
    ItemCount: StrictInt | None = None
    KeySchema: list[SecurityHubAwsDynamoDbTableKeySchema] | None = None
    Projection: SecurityHubAwsDynamoDbTableProjection | None = None
    ProvisionedThroughput: SecurityHubAwsDynamoDbTableProvisionedThroughput | None = None
