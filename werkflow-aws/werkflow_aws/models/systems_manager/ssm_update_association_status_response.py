from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_association_description import SSMAssociationDescription


class SSMUpdateAssociationStatusResponse(BaseModel):
    AssociationDescription: SSMAssociationDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
