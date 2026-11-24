from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_bulk_operation_table_detail import DynamoDBBulkOperationTableDetail
from .dynamo_db_bulk_operation_usage import DynamoDBBulkOperationUsage
from .dynamo_db_input_s3_configuration import DynamoDBInputS3Configuration
from .dynamo_db_output_s3_configuration import DynamoDBOutputS3Configuration


class DynamoDBBulkOperationDescription(BaseModel):
    BulkOperationArn: StrictStr | None = None
    BulkOperationStatus: StrictStr | None = None
    TableDetails: list[DynamoDBBulkOperationTableDetail] | None = None
    ClientToken: StrictStr | None = None
    InputS3Configuration: DynamoDBInputS3Configuration | None = None
    OutputS3Configuration: DynamoDBOutputS3Configuration | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ProcessedItemCount: StrictInt | None = None
    ProcessedInputBytes: StrictInt | None = None
    TotalInputBytes: StrictInt | None = None
    BulkOperationUsage: list[DynamoDBBulkOperationUsage] | None = None
    FailedItemCount: StrictInt | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    MaxWriteRequestUnits: StrictInt | None = None
    PerformanceTier: StrictStr | None = None
