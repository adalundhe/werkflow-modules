from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictStr
from .included_fields import IncludedFields
from .issue_transition import IssueTransition
from .issue_update_metadata import IssueUpdateMetadata
from .json_type_bean import JsonTypeBean
from .operations import Operations
from .page_of_changelogs import PageOfChangelogs


class IssueBean(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    changelog: PageOfChangelogs | None = None
    editmeta: IssueUpdateMetadata | None = None
    expand: StrictStr | None = None
    fields: dict[StrictStr, Any] | None = None
    fieldsToInclude: IncludedFields | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    names: dict[StrictStr, StrictStr] | None = None
    operations: Operations | None = None
    properties: dict[StrictStr, Any] | None = None
    renderedFields: dict[StrictStr, Any] | None = None
    schema_: dict[StrictStr, JsonTypeBean] | None = PydanticField(default=None, alias='schema')
    self: StrictStr | None = None
    transitions: list[IssueTransition] | None = None
    versionedRepresentations: dict[StrictStr, dict[StrictStr, Any]] | None = None
