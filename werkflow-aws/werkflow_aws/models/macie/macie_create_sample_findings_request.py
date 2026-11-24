from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieCreateSampleFindingsRequest(BaseModel):
    findingTypes: list[Literal['SensitiveData:S3Object/Multiple', 'SensitiveData:S3Object/Financial', 'SensitiveData:S3Object/Personal', 'SensitiveData:S3Object/Credentials', 'SensitiveData:S3Object/CustomIdentifier', 'Policy:IAMUser/S3BucketPublic', 'Policy:IAMUser/S3BucketSharedExternally', 'Policy:IAMUser/S3BucketReplicatedExternally', 'Policy:IAMUser/S3BucketEncryptionDisabled', 'Policy:IAMUser/S3BlockPublicAccessDisabled', 'Policy:IAMUser/S3BucketSharedWithCloudFront']] | None = None
