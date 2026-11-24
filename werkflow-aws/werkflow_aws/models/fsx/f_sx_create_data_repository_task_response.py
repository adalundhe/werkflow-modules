from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .f_sx_data_repository_task import FSxDataRepositoryTask


class FSxCreateDataRepositoryTaskResponse(BaseModel):
    DataRepositoryTask: FSxDataRepositoryTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
