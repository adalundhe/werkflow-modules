from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_context_provider_key_definition import IAMContextProviderKeyDefinition


class IAMContextProvider(BaseModel):
    KeyDefinitionList: list[IAMContextProviderKeyDefinition] | None = None
    SubjectSourceKey: StrictStr | None = None
    SubjectTypeValue: StrictStr | None = None
    SubjectTypeSourceKey: StrictStr | None = None
