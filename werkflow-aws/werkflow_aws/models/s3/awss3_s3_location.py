from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .awss3_encryption import AWSS3Encryption
from .awss3_grant_input import AWSS3GrantInput
from .awss3_metadata_entry import AWSS3MetadataEntry
from .awss3_tagging import AWSS3Tagging


class AWSS3S3Location(BaseModel):
    BucketName: StrictStr
    Prefix: StrictStr
    Encryption: AWSS3Encryption | None = None
    CannedACL: Literal['private', 'public-read', 'public-read-write', 'authenticated-read', 'aws-exec-read', 'bucket-owner-read', 'bucket-owner-full-control'] | None = None
    AccessControlList: list[AWSS3GrantInput] | None = None
    Tagging: AWSS3Tagging | None = None
    UserMetadata: list[AWSS3MetadataEntry] | None = None
    StorageClass: Literal['STANDARD', 'REDUCED_REDUNDANCY', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'GLACIER', 'DEEP_ARCHIVE', 'OUTPOSTS', 'GLACIER_IR', 'SNOW', 'EXPRESS_ONEZONE', 'FSX_OPENZFS', 'FSX_ONTAP', 'AWS_BACKUP_WARM', 'AWS_BACKUP_LOW_COST_WARM'] | None = None
