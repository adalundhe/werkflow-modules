from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class CodeCommitGetBlobResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    content: StrictBytes | Any | None = None
    ResponseMetadata: dict[str, Any] | None = None
