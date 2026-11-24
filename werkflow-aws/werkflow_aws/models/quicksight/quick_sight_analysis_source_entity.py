from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_analysis_source_template import QuickSightAnalysisSourceTemplate


class QuickSightAnalysisSourceEntity(BaseModel):
    SourceTemplate: QuickSightAnalysisSourceTemplate | None = None
