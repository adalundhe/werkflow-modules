from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_template_source_entity import QuickSightTemplateSourceEntity
from .quick_sight_template_version_definition import QuickSightTemplateVersionDefinition
from .quick_sight_validation_strategy import QuickSightValidationStrategy


class QuickSightUpdateTemplateRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    SourceEntity: QuickSightTemplateSourceEntity | None = None
    VersionDescription: StrictStr | None = None
    Name: StrictStr | None = None
    Definition: QuickSightTemplateVersionDefinition | None = None
    ValidationStrategy: QuickSightValidationStrategy | None = None
