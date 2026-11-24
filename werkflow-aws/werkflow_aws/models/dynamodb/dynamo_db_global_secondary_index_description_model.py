from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dynamo_db_global_secondary_index_warm_throughput_description_model import DynamoDBGlobalSecondaryIndexWarmThroughputDescriptionModel
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_projection_model import DynamoDBProjectionModel
from .dynamo_db_provisioned_throughput_description_model import DynamoDBProvisionedThroughputDescriptionModel


class DynamoDBGlobalSecondaryIndexDescriptionModel(BaseModel):
    IndexName: StrictStr | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    Projection: DynamoDBProjectionModel | None = None
    IndexStatus: StrictStr | None = None
    Backfilling: StrictBool | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputDescriptionModel | None = None
    IndexSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    IndexArn: StrictStr | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughputModel | None = None
    WarmThroughput: DynamoDBGlobalSecondaryIndexWarmThroughputDescriptionModel | None = None
