from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_projection_model import DynamoDBProjectionModel
from .dynamo_db_provisioned_throughput_model import DynamoDBProvisionedThroughputModel


class DynamoDBGlobalSecondaryIndexInfo(BaseModel):
    IndexName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    Projection: DynamoDBProjectionModel | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputModel | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughputModel | None = None
