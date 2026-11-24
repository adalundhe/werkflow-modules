from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTDescribeProvisioningTemplateVersionResponse(BaseModel):
    versionId: StrictInt | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    templateBody: StrictStr | None = None
    isDefaultVersion: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
