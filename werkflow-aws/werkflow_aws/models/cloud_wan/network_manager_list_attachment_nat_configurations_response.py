from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .network_manager_attachment_nat_configuration import NetworkManagerAttachmentNatConfiguration


class NetworkManagerListAttachmentNatConfigurationsResponse(BaseModel):
    AttachmentNatConfigurations: list[NetworkManagerAttachmentNatConfiguration] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
