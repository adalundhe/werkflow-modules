from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_s3_path import KendraS3Path


class KendraOneDriveUsers(BaseModel):
    OneDriveUserList: list[StrictStr] | None = None
    OneDriveUserS3Path: KendraS3Path | None = None
