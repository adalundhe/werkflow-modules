from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_data_repository_association import FSxDataRepositoryAssociation


class FSxUpdateDataRepositoryAssociationResponse(BaseModel):
    Association: FSxDataRepositoryAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
