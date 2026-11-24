from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .dynamo_db_capacity import DynamoDBCapacity
from .dynamo_db_vector_capacity import DynamoDBVectorCapacity


class DynamoDBConsumedCapacity(BaseModel):
    TableName: StrictStr | None = None
    CapacityUnits: StrictFloat | StrictInt | None = None
    ReadCapacityUnits: StrictFloat | StrictInt | None = None
    WriteCapacityUnits: StrictFloat | StrictInt | None = None
    Table: DynamoDBCapacity | None = None
    LocalSecondaryIndexes: dict[StrictStr, DynamoDBCapacity] | None = None
    GlobalSecondaryIndexes: dict[StrictStr, DynamoDBCapacity] | None = None
    VectorIndexes: dict[StrictStr, DynamoDBVectorCapacity] | None = None
