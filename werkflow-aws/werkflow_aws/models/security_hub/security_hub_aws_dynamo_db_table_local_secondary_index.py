from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_dynamo_db_table_key_schema import SecurityHubAwsDynamoDbTableKeySchema
from .security_hub_aws_dynamo_db_table_projection import SecurityHubAwsDynamoDbTableProjection


class SecurityHubAwsDynamoDbTableLocalSecondaryIndex(BaseModel):
    IndexArn: StrictStr | None = None
    IndexName: StrictStr | None = None
    KeySchema: list[SecurityHubAwsDynamoDbTableKeySchema] | None = None
    Projection: SecurityHubAwsDynamoDbTableProjection | None = None
