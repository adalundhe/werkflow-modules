from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_s3_object_tag import EC2S3ObjectTag


class EC2CreateStoreImageTaskRequest(BaseModel):
    ImageId: StrictStr
    Bucket: StrictStr
    S3ObjectTags: list[EC2S3ObjectTag] | None = None
    DryRun: StrictBool | None = None
