from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_input_format_options import DynamoDBInputFormatOptions
from .dynamo_dbs3_bucket_source import DynamoDBS3BucketSource
from .dynamo_db_table_creation_parameters import DynamoDBTableCreationParameters


class DynamoDBImportTableDescription(BaseModel):
    ImportArn: StrictStr | None = None
    ImportStatus: StrictStr | None = None
    TableArn: StrictStr | None = None
    TableId: StrictStr | None = None
    ClientToken: StrictStr | None = None
    S3BucketSource: DynamoDBS3BucketSource | None = None
    ErrorCount: StrictInt | None = None
    CloudWatchLogGroupArn: StrictStr | None = None
    InputFormat: StrictStr | None = None
    InputFormatOptions: DynamoDBInputFormatOptions | None = None
    InputCompressionType: StrictStr | None = None
    TableCreationParameters: DynamoDBTableCreationParameters | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ProcessedSizeBytes: StrictInt | None = None
    ProcessedItemCount: StrictInt | None = None
    ImportedItemCount: StrictInt | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
