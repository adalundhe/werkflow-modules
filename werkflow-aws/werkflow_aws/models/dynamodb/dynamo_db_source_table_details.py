from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_key_schema_element_model import DynamoDBKeySchemaElementModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_provisioned_throughput_model import DynamoDBProvisionedThroughputModel


class DynamoDBSourceTableDetails(BaseModel):
    TableName: StrictStr | None = None
    TableId: StrictStr | None = None
    TableArn: StrictStr | None = None
    TableSizeBytes: StrictInt | None = None
    KeySchema: list[DynamoDBKeySchemaElementModel] | None = None
    TableCreationDateTime: datetime.datetime | StrictStr | None = None
    ProvisionedThroughput: DynamoDBProvisionedThroughputModel | None = None
    OnDemandThroughput: DynamoDBOnDemandThroughputModel | None = None
    ItemCount: StrictInt | None = None
    BillingMode: StrictStr | None = None
