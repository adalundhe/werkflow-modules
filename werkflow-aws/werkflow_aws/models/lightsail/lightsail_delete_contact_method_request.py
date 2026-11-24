from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LightsailDeleteContactMethodRequest(BaseModel):
    protocol: Literal['Email', 'SMS']
