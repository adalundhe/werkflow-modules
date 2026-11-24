from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LightsailGetContactMethodsRequest(BaseModel):
    protocols: list[Literal['Email', 'SMS']] | None = None
