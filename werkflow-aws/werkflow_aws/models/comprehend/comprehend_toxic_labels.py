from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .comprehend_toxic_content import ComprehendToxicContent


class ComprehendToxicLabels(BaseModel):
    Labels: list[ComprehendToxicContent] | None = None
    Toxicity: StrictFloat | StrictInt | None = None
