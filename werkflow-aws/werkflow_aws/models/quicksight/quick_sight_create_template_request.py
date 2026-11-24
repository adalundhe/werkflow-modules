from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission
from .quick_sight_tag import QuickSightTag
from .quick_sight_template_source_entity import QuickSightTemplateSourceEntity
from .quick_sight_template_version_definition import QuickSightTemplateVersionDefinition
from .quick_sight_validation_strategy import QuickSightValidationStrategy


class QuickSightCreateTemplateRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    Name: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    SourceEntity: QuickSightTemplateSourceEntity | None = None
    Tags: list[QuickSightTag] | None = None
    VersionDescription: StrictStr | None = None
    Definition: QuickSightTemplateVersionDefinition | None = None
    ValidationStrategy: QuickSightValidationStrategy | None = None
