from __future__ import annotations
from pydantic import BaseModel
from .kendra_template import KendraTemplate


class KendraTemplateConfiguration(BaseModel):
    Template: KendraTemplate | None = None
