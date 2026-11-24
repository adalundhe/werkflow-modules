from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_data_repository_association import FSxDataRepositoryAssociation


class FSxDescribeDataRepositoryAssociationsResponse(BaseModel):
    Associations: list[FSxDataRepositoryAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
