from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dynamo_db_capacity_model import DynamoDBCapacityModel
from .dynamo_db_vector_capacity_model import DynamoDBVectorCapacityModel


class DynamoDBConsumedCapacityModel(BaseModel):
    TableName: StrictStr | None = None
    CapacityUnits: StrictFloat | StrictInt | None = None
    ReadCapacityUnits: StrictFloat | StrictInt | None = None
    WriteCapacityUnits: StrictFloat | StrictInt | None = None
    Table: DynamoDBCapacityModel | None = None
    LocalSecondaryIndexes: dict[StrictStr, DynamoDBCapacityModel] | None = None
    GlobalSecondaryIndexes: dict[StrictStr, DynamoDBCapacityModel] | None = None
    VectorIndexes: dict[StrictStr, DynamoDBVectorCapacityModel] | None = None
