from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OpenSearchNaturalLanguageQueryGenerationOptionsInput(BaseModel):
    DesiredState: Literal['ENABLED', 'DISABLED'] | None = None
