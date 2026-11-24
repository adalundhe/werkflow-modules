from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dynamo_db_attribute_value_model import DynamoDBAttributeValueModel
from .dynamo_db_batch_statement_error import DynamoDBBatchStatementError


class DynamoDBBatchStatementResponse(BaseModel):
    Error: DynamoDBBatchStatementError | None = None
    TableName: StrictStr | None = None
    Item: dict[StrictStr, DynamoDBAttributeValueModel] | None = None
