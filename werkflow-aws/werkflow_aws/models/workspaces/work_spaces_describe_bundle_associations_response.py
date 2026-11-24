from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_bundle_resource_association import WorkSpacesBundleResourceAssociation


class WorkSpacesDescribeBundleAssociationsResponse(BaseModel):
    Associations: list[WorkSpacesBundleResourceAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
