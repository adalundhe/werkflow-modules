from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_template_source_analysis import QuickSightTemplateSourceAnalysis
from .quick_sight_template_source_template import QuickSightTemplateSourceTemplate


class QuickSightTemplateSourceEntity(BaseModel):
    SourceAnalysis: QuickSightTemplateSourceAnalysis | None = None
    SourceTemplate: QuickSightTemplateSourceTemplate | None = None
