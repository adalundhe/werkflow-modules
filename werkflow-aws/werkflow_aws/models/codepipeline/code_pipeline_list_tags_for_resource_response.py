from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_tag import CodePipelineTag


class CodePipelineListTagsForResourceResponse(BaseModel):
    tags: list[CodePipelineTag] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
