from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_mitigation_action_identifier import IoTMitigationActionIdentifier


class IoTListMitigationActionsResponse(BaseModel):
    actionIdentifiers: list[IoTMitigationActionIdentifier] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
