from __future__ import annotations
from pydantic import BaseModel
from .field_configuration_to_issue_type_mapping import FieldConfigurationToIssueTypeMapping


class AssociateFieldConfigurationsWithIssueTypesRequest(BaseModel):
    mappings: list[FieldConfigurationToIssueTypeMapping] | None = None
