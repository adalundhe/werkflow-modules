from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .iam_inline_policy import IAMInlinePolicy
from .iam_parameter_definition import IAMParameterDefinition
from .iam_tag_template import IAMTagTemplate


class IAMRoleTemplateVersion(BaseModel):
    TemplateArn: StrictStr | None = None
    TemplateName: StrictStr | None = None
    TemplateVersionId: StrictStr | None = None
    Description: StrictStr | None = None
    MajorVersion: StrictInt | None = None
    DefaultMinorVersion: StrictInt | None = None
    ManagedByType: StrictStr | None = None
    ManagedByValue: StrictStr | None = None
    Enabled: StrictBool | None = None
    MinorVersion: StrictInt | None = None
    RoleNamePattern: StrictStr | None = None
    RolePathPattern: StrictStr | None = None
    RoleDescriptionPattern: StrictStr | None = None
    AssumeRolePolicyDocumentTemplate: StrictStr | None = None
    InlinePolicyTemplates: list[IAMInlinePolicy] | None = None
    ManagedPolicyArns: list[StrictStr] | None = None
    PermissionBoundaryArn: StrictStr | None = None
    ParametersDefinition: list[IAMParameterDefinition] | None = None
    RoleTagsTemplate: list[IAMTagTemplate] | None = None
    MaxSessionDuration: StrictInt | None = None
    VersionEnabled: StrictBool | None = None
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    UpdateTimestamp: datetime.datetime | StrictStr | None = None
