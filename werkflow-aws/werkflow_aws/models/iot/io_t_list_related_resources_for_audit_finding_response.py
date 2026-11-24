from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_related_resource import IoTRelatedResource


class IoTListRelatedResourcesForAuditFindingResponse(BaseModel):
    relatedResources: list[IoTRelatedResource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
