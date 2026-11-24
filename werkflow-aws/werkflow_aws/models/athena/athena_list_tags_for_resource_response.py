from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_tag_model import AthenaTagModel


class AthenaListTagsForResourceResponse(BaseModel):
    Tags: list[AthenaTagModel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
