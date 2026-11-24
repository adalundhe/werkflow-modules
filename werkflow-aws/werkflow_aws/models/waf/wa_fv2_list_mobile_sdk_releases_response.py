from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_release_summary import WAFv2ReleaseSummary


class WAFv2ListMobileSdkReleasesResponse(BaseModel):
    ReleaseSummaries: list[WAFv2ReleaseSummary] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
