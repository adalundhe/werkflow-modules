from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_association import RedshiftAssociation


class RedshiftDescribeCustomDomainAssociationsResponse(BaseModel):
    Marker: StrictStr | None = None
    Associations: list[RedshiftAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
