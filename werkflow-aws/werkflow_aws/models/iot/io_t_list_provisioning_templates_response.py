from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_provisioning_template_summary import IoTProvisioningTemplateSummary


class IoTListProvisioningTemplatesResponse(BaseModel):
    templates: list[IoTProvisioningTemplateSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
