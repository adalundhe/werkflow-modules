from __future__ import annotations
from pydantic import BaseModel
from .dynamo_db_global_secondary_index_info import DynamoDBGlobalSecondaryIndexInfo
from .dynamo_db_local_secondary_index_info import DynamoDBLocalSecondaryIndexInfo
from .dynamo_dbsse_description_model import DynamoDBSSEDescriptionModel
from .dynamo_db_stream_specification_model import DynamoDBStreamSpecificationModel
from .dynamo_db_time_to_live_description_model import DynamoDBTimeToLiveDescriptionModel
from .dynamo_db_vector_index_info import DynamoDBVectorIndexInfo


class DynamoDBSourceTableFeatureDetails(BaseModel):
    LocalSecondaryIndexes: list[DynamoDBLocalSecondaryIndexInfo] | None = None
    GlobalSecondaryIndexes: list[DynamoDBGlobalSecondaryIndexInfo] | None = None
    StreamDescription: DynamoDBStreamSpecificationModel | None = None
    TimeToLiveDescription: DynamoDBTimeToLiveDescriptionModel | None = None
    SSEDescription: DynamoDBSSEDescriptionModel | None = None
    VectorIndexes: list[DynamoDBVectorIndexInfo] | None = None
