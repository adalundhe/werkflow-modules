from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_input_s3_configuration import DynamoDBInputS3Configuration
from .dynamo_db_output_s3_configuration import DynamoDBOutputS3Configuration


class DynamoDBStartBulkPutItemsRequest(BaseModel):
    InputS3Configuration: DynamoDBInputS3Configuration
    OutputS3Configuration: DynamoDBOutputS3Configuration
    TableName: StrictStr
    ClientToken: StrictStr | None = None
    MaxWriteRequestUnits: StrictInt | None = None
    PerformanceTier: Literal['STANDARD', 'ACCELERATED'] | None = None
