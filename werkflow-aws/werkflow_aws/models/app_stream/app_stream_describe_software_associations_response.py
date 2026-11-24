from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_software_associations import AppStreamSoftwareAssociations


class AppStreamDescribeSoftwareAssociationsResponse(BaseModel):
    AssociatedResource: StrictStr | None = None
    SoftwareAssociations: list[AppStreamSoftwareAssociations] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
