from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_provisioning_hook import IoTProvisioningHook


class IoTDescribeProvisioningTemplateResponse(BaseModel):
    templateArn: StrictStr | None = None
    templateName: StrictStr | None = None
    description: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
    lastModifiedDate: datetime.datetime | StrictStr | None = None
    defaultVersionId: StrictInt | None = None
    templateBody: StrictStr | None = None
    enabled: StrictBool | None = None
    provisioningRoleArn: StrictStr | None = None
    preProvisioningHook: IoTProvisioningHook | None = None
    type: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
