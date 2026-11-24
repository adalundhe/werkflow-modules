from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .athena_capacity_assignment_configuration import AthenaCapacityAssignmentConfiguration


class AthenaGetCapacityAssignmentConfigurationResponse(BaseModel):
    CapacityAssignmentConfiguration: AthenaCapacityAssignmentConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
