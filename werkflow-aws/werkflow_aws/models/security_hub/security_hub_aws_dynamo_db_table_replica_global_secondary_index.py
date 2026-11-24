from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_dynamo_db_table_provisioned_throughput_override import SecurityHubAwsDynamoDbTableProvisionedThroughputOverride


class SecurityHubAwsDynamoDbTableReplicaGlobalSecondaryIndex(BaseModel):
    IndexName: StrictStr | None = None
    ProvisionedThroughputOverride: SecurityHubAwsDynamoDbTableProvisionedThroughputOverride | None = None
