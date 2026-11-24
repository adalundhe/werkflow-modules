from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emros_release import EMROSRelease
from .emr_simplified_application import EMRSimplifiedApplication


class EMRDescribeReleaseLabelResponse(BaseModel):
    ReleaseLabel: StrictStr | None = None
    Applications: list[EMRSimplifiedApplication] | None = None
    NextToken: StrictStr | None = None
    AvailableOSReleases: list[EMROSRelease] | None = None
    ResponseMetadata: dict[str, Any] | None = None
