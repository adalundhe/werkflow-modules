from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class TextractHumanLoopDataAttributes(BaseModel):
    ContentClassifiers: list[Literal['FreeOfPersonallyIdentifiableInformation', 'FreeOfAdultContent']] | None = None
