from __future__ import annotations
from pydantic import BaseModel
from .contextual_configuration import ContextualConfiguration


class CustomFieldConfigurations(BaseModel):
    configurations: list[ContextualConfiguration] | None = None
