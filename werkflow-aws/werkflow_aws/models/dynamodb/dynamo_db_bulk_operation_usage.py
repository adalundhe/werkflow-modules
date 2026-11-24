from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_bulk_operation_bytes import DynamoDBBulkOperationBytes
from .dynamo_db_bulk_operation_vector_bytes import DynamoDBBulkOperationVectorBytes


class DynamoDBBulkOperationUsage(BaseModel):
    TableName: StrictStr | None = None
    BulkPutBytes: StrictInt | None = None
    Table: DynamoDBBulkOperationBytes | None = None
    LocalSecondaryIndexes: dict[StrictStr, DynamoDBBulkOperationBytes] | None = None
    GlobalSecondaryIndexes: dict[StrictStr, DynamoDBBulkOperationBytes] | None = None
    VectorIndexes: dict[StrictStr, DynamoDBBulkOperationVectorBytes] | None = None
