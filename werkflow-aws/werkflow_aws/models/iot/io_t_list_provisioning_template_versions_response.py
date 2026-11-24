from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_provisioning_template_version_summary import IoTProvisioningTemplateVersionSummary


class IoTListProvisioningTemplateVersionsResponse(BaseModel):
    versions: list[IoTProvisioningTemplateVersionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
