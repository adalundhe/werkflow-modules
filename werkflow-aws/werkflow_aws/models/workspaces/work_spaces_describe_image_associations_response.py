from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_image_resource_association import WorkSpacesImageResourceAssociation


class WorkSpacesDescribeImageAssociationsResponse(BaseModel):
    Associations: list[WorkSpacesImageResourceAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
