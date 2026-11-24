from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .dynamo_db_filter_specification import DynamoDBFilterSpecification
from .dynamo_db_incremental_export_specification import DynamoDBIncrementalExportSpecification


class DynamoDBExportTableToPointInTimeRequest(BaseModel):
    TableArn: StrictStr
    S3Bucket: StrictStr
    ExportTime: datetime.datetime | StrictStr | None = None
    ClientToken: StrictStr | None = None
    S3BucketOwner: StrictStr | None = None
    S3Prefix: StrictStr | None = None
    S3SseAlgorithm: Literal['AES256', 'KMS'] | None = None
    S3SseKmsKeyId: StrictStr | None = None
    ExportFormat: Literal['DYNAMODB_JSON', 'ION'] | None = None
    ExportType: Literal['FULL_EXPORT', 'INCREMENTAL_EXPORT'] | None = None
    IncrementalExportSpecification: DynamoDBIncrementalExportSpecification | None = None
    FilterSpecification: DynamoDBFilterSpecification | None = None
