from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_tag import IAMTag


class IAMPolicy(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyId: StrictStr | None = None
    Arn: StrictStr | None = None
    Path: StrictStr | None = None
    DefaultVersionId: StrictStr | None = None
    AttachmentCount: StrictInt | None = None
    PermissionsBoundaryUsageCount: StrictInt | None = None
    IsAttachable: StrictBool | None = None
    Description: StrictStr | None = None
    CreateDate: datetime.datetime | None = None
    UpdateDate: datetime.datetime | None = None
    Tags: list[IAMTag] | None = None
