from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_encryption_configuration import DataZoneEncryptionConfiguration


class DataZoneGetDataExportConfigurationResponse(BaseModel):
    isExportEnabled: StrictBool | None = None
    status: StrictStr | None = None
    encryptionConfiguration: DataZoneEncryptionConfiguration | None = None
    s3TableBucketArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
