from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_association_version_info import SSMAssociationVersionInfo


class SSMListAssociationVersionsResponse(BaseModel):
    AssociationVersions: list[SSMAssociationVersionInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
