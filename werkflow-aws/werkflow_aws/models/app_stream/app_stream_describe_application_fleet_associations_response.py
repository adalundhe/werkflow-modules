from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_application_fleet_association import AppStreamApplicationFleetAssociation


class AppStreamDescribeApplicationFleetAssociationsResponse(BaseModel):
    ApplicationFleetAssociations: list[AppStreamApplicationFleetAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
