from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_association_description import SSMAssociationDescription
from .ssm_failed_create_association import SSMFailedCreateAssociation


class SSMCreateAssociationBatchResponse(BaseModel):
    Successful: list[SSMAssociationDescription] | None = None
    Failed: list[SSMFailedCreateAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
