from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_projection import DynamoDBProjection
from .dynamo_db_provisioned_throughput import DynamoDBProvisionedThroughput
from .dynamo_db_warm_throughput import DynamoDBWarmThroughput


class DynamoDBCreateGlobalSecondaryIndexAction(BaseModel):
    IndexName: StrictStr
    KeySchema: list[DynamoDBKeySchemaElement]
    Projection: DynamoDBProjection
    ProvisionedThroughput: DynamoDBProvisionedThroughput | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    WarmThroughput: DynamoDBWarmThroughput | None = None
