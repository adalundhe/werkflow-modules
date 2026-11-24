from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dynamo_dbs3_bucket_source import DynamoDBS3BucketSource


class DynamoDBImportSummary(BaseModel):
    ImportArn: StrictStr | None = None
    ImportStatus: StrictStr | None = None
    TableArn: StrictStr | None = None
    S3BucketSource: DynamoDBS3BucketSource | None = None
    CloudWatchLogGroupArn: StrictStr | None = None
    InputFormat: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
