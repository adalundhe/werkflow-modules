from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_flow_destination_field_properties import AppFlowDestinationFieldProperties
from .app_flow_source_field_properties import AppFlowSourceFieldProperties
from .app_flow_supported_field_type_details import AppFlowSupportedFieldTypeDetails


class AppFlowConnectorEntityField(BaseModel):
    identifier: StrictStr | None = None
    parentIdentifier: StrictStr | None = None
    label: StrictStr | None = None
    isPrimaryKey: StrictBool | None = None
    defaultValue: StrictStr | None = None
    isDeprecated: StrictBool | None = None
    supportedFieldTypeDetails: AppFlowSupportedFieldTypeDetails | None = None
    description: StrictStr | None = None
    sourceProperties: AppFlowSourceFieldProperties | None = None
    destinationProperties: AppFlowDestinationFieldProperties | None = None
    customProperties: dict[StrictStr, StrictStr] | None = None
