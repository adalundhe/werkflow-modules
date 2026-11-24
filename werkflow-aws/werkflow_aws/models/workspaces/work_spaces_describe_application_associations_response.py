from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_application_resource_association import WorkSpacesApplicationResourceAssociation


class WorkSpacesDescribeApplicationAssociationsResponse(BaseModel):
    Associations: list[WorkSpacesApplicationResourceAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
