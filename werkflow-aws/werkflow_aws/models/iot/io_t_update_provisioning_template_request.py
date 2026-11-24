from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_provisioning_hook import IoTProvisioningHook


class IoTUpdateProvisioningTemplateRequest(BaseModel):
    templateName: StrictStr
    description: StrictStr | None = None
    enabled: StrictBool | None = None
    defaultVersionId: StrictInt | None = None
    provisioningRoleArn: StrictStr | None = None
    preProvisioningHook: IoTProvisioningHook | None = None
    removePreProvisioningHook: StrictBool | None = None
