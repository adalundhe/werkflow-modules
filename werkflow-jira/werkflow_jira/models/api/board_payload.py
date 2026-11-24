from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .board_column_payload import BoardColumnPayload
from .board_feature_payload import BoardFeaturePayload
from .card_layout import CardLayout
from .card_layout_field import CardLayoutField
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .quick_filter_payload import QuickFilterPayload
from .swimlanes_payload import SwimlanesPayload
from .working_days_config import WorkingDaysConfig


class BoardPayload(BaseModel):
    boardFilterJQL: StrictStr | None = None
    cardColorStrategy: StrictStr | None = None
    cardLayout: CardLayout | None = None
    cardLayouts: list[CardLayoutField] | None = None
    columns: list[BoardColumnPayload] | None = None
    enableCardCover: StrictBool | None = None
    features: list[BoardFeaturePayload] | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    quickFilters: list[QuickFilterPayload] | None = None
    supportsSprint: StrictBool | None = None
    swimlanes: SwimlanesPayload | None = None
    workingDaysConfig: WorkingDaysConfig | None = None
