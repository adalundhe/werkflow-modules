from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_custom_values_configuration import QuickSightCustomValuesConfiguration


class QuickSightDestinationParameterValueConfiguration(BaseModel):
    CustomValuesConfiguration: QuickSightCustomValuesConfiguration | None = None
    SelectAllValueOptions: StrictStr | None = None
    SourceParameterName: StrictStr | None = None
    SourceField: StrictStr | None = None
    SourceColumn: QuickSightColumnIdentifier | None = None
