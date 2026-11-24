from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_application_fleet_association import AppStreamApplicationFleetAssociation


class AppStreamAssociateApplicationFleetResponse(BaseModel):
    ApplicationFleetAssociation: AppStreamApplicationFleetAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
