from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_association import SSMAssociation


class SSMListAssociationsResponse(BaseModel):
    Associations: list[SSMAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
