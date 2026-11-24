from __future__ import annotations
from pydantic import BaseModel
from .personalize_fields_for_theme_generation import PersonalizeFieldsForThemeGeneration


class PersonalizeThemeGenerationConfig(BaseModel):
    fieldsForThemeGeneration: PersonalizeFieldsForThemeGeneration | None = None
