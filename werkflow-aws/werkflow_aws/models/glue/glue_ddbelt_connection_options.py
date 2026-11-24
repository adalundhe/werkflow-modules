from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueDDBELTConnectionOptions(BaseModel):
    DynamodbExport: StrictStr | None = None
    DynamodbUnnestDDBJson: StrictBool | None = None
    DynamodbTableArn: StrictStr | None = None
    DynamodbS3Bucket: StrictStr | None = None
    DynamodbS3Prefix: StrictStr | None = None
    DynamodbS3BucketOwner: StrictStr | None = None
    DynamodbStsRoleArn: StrictStr | None = None
