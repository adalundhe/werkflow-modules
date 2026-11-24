from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_database import GlueDatabase


class GlueGetDatabaseResponse(BaseModel):
    Database: GlueDatabase | None = None
    ResponseMetadata: dict[str, Any] | None = None
