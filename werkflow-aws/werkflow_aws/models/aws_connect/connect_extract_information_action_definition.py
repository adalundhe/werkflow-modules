from __future__ import annotations
from pydantic import BaseModel
from .connect_rules_extraction_definition_identifier import ConnectRulesExtractionDefinitionIdentifier


class ConnectExtractInformationActionDefinition(BaseModel):
    RulesExtractionDefinitions: list[ConnectRulesExtractionDefinitionIdentifier] | None = None
