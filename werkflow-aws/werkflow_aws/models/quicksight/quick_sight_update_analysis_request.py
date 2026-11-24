from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_analysis_definition import QuickSightAnalysisDefinition
from .quick_sight_analysis_source_entity import QuickSightAnalysisSourceEntity
from .quick_sight_parameters import QuickSightParameters
from .quick_sight_validation_strategy import QuickSightValidationStrategy


class QuickSightUpdateAnalysisRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
    Name: StrictStr
    Parameters: QuickSightParameters | None = None
    SourceEntity: QuickSightAnalysisSourceEntity | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightAnalysisDefinition | None = None
    ValidationStrategy: QuickSightValidationStrategy | None = None
