from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_global_secondary_index_warm_throughput_description import DynamoDBGlobalSecondaryIndexWarmThroughputDescription
from .dynamo_db_index_status import DynamoDBIndexStatus
from .dynamo_db_key_schema_element import DynamoDBKeySchemaElement
from .dynamo_db_on_demand_throughput import DynamoDBOnDemandThroughput
from .dynamo_db_projection import DynamoDBProjection
from .dynamo_db_provisioned_throughput_description import DynamoDBProvisionedThroughputDescription


class DynamoDBGlobalSecondaryIndexDescription(BaseModel):
    IndexName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElement] | None = None
    Projection: DynamoDBProjection | None = None
    IndexStatus: DynamoDBIndexStatus | None = None
    Backfilling: StrictBool | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputDescription | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughput | None = None
    WarmThroughput: DynamoDBGlobalSecondaryIndexWarmThroughputDescription | None = None
