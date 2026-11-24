from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_client_properties_result import WorkSpacesClientPropertiesResult


class WorkSpacesDescribeClientPropertiesResponse(BaseModel):
    ClientPropertiesList: list[WorkSpacesClientPropertiesResult] | None = None
    ResponseMetadata: dict[str, Any] | None = None
