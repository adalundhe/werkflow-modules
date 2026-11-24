from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes


class TranslatedDocument(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Content: StrictBytes | Any | None = None
