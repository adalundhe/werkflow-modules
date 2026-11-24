from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .dynamo_db_global_secondary_index_model import DynamoDBGlobalSecondaryIndexModel
from .dynamo_db_local_secondary_index_model import DynamoDBLocalSecondaryIndexModel
from .dynamo_db_on_demand_throughput_model import DynamoDBOnDemandThroughputModel
from .dynamo_db_provisioned_throughput_model import DynamoDBProvisionedThroughputModel
from .dynamo_dbsse_specification_model import DynamoDBSSESpecificationModel
from .dynamo_db_vector_index_model import DynamoDBVectorIndexModel


class DynamoDBRestoreTableToPointInTimeRequest(BaseModel):
    TargetTableName: StrictStr
    SourceTableArn: StrictStr | None = None
    SourceTableName: StrictStr | None = None
    UseLatestRestorableTime: StrictBool | None = None
    RestoreDateTime: datetime.datetime | StrictStr | None = None
    BillingModeOverride: Literal['PROVISIONED', 'PAY_PER_REQUEST'] | None = None
    GlobalSecondaryIndexOverride: list[DynamoDBGlobalSecondaryIndexModel] | None = None
    LocalSecondaryIndexOverride: list[DynamoDBLocalSecondaryIndexModel] | None = None
    ProvisionedThroughputOverride: DynamoDBProvisionedThroughputModel | None = None
    OnDemandThroughputOverride: DynamoDBOnDemandThroughputModel | None = None
    SSESpecificationOverride: DynamoDBSSESpecificationModel | None = None
    VectorIndexOverride: list[DynamoDBVectorIndexModel] | None = None
