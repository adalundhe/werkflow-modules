from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .dynamo_db_filter_specification import DynamoDBFilterSpecification
from .dynamo_db_incremental_export_specification import DynamoDBIncrementalExportSpecification


class DynamoDBExportDescription(BaseModel):
    ExportArn: StrictStr | None = None
    ExportStatus: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ExportManifest: StrictStr | None = None
    TableArn: StrictStr | None = None
    TableId: StrictStr | None = None
    ExportTime: datetime.datetime | StrictStr | None = None
    ClientToken: StrictStr | None = None
    S3Bucket: StrictStr | None = None
    S3BucketOwner: StrictStr | None = None
    S3Prefix: StrictStr | None = None
    S3SseAlgorithm: StrictStr | None = None
    S3SseKmsKeyId: StrictStr | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    ExportFormat: StrictStr | None = None
    BilledSizeBytes: StrictInt | None = None
    ItemCount: StrictInt | None = None
    ExportType: StrictStr | None = None
    IncrementalExportSpecification: DynamoDBIncrementalExportSpecification | None = None
    FilterSpecification: DynamoDBFilterSpecification | None = None
