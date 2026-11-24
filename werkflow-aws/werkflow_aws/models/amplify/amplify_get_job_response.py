from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_job import AmplifyJob


class AmplifyGetJobResponse(BaseModel):
    job: AmplifyJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
