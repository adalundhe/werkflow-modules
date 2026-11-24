from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dynamo_db_input_format_options import DynamoDBInputFormatOptions
from .dynamo_dbs3_bucket_source import DynamoDBS3BucketSource
from .dynamo_db_table_creation_parameters import DynamoDBTableCreationParameters


class DynamoDBImportTableRequest(BaseModel):
    S3BucketSource: DynamoDBS3BucketSource
    InputFormat: Literal['DYNAMODB_JSON', 'ION', 'CSV']
    TableCreationParameters: DynamoDBTableCreationParameters
    ClientToken: StrictStr | None = None
    InputFormatOptions: DynamoDBInputFormatOptions | None = None
    InputCompressionType: Literal['GZIP', 'ZSTD', 'NONE'] | None = None
