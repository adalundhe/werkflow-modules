from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_provisioning_hook import IoTProvisioningHook
from .io_t_tag import IoTTag


class IoTCreateProvisioningTemplateRequest(BaseModel):
    templateName: StrictStr
    templateBody: StrictStr
    provisioningRoleArn: StrictStr
    description: StrictStr | None = None
    enabled: StrictBool | None = None
    preProvisioningHook: IoTProvisioningHook | None = None
    tags: list[IoTTag] | None = None
    type: Literal['FLEET_PROVISIONING', 'JITP'] | None = None
