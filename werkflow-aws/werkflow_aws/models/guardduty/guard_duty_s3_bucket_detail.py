from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .guard_duty_default_server_side_encryption import GuardDutyDefaultServerSideEncryption
from .guard_duty_owner import GuardDutyOwner
from .guard_duty_public_access import GuardDutyPublicAccess
from .guard_duty_s3_object_detail import GuardDutyS3ObjectDetail
from .guard_duty_tag import GuardDutyTag


class GuardDutyS3BucketDetail(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    Owner: GuardDutyOwner | None = None
    Tags: list[GuardDutyTag] | None = None
    DefaultServerSideEncryption: GuardDutyDefaultServerSideEncryption | None = None
    PublicAccess: GuardDutyPublicAccess | None = None
    S3ObjectDetails: list[GuardDutyS3ObjectDetail] | None = None
