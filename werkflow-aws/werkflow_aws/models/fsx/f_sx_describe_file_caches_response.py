from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_file_cache import FSxFileCache


class FSxDescribeFileCachesResponse(BaseModel):
    FileCaches: list[FSxFileCache] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
