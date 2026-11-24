from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glacier_job_description import GlacierJobDescription


class GlacierListJobsResponse(BaseModel):
    JobList: list[GlacierJobDescription] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
