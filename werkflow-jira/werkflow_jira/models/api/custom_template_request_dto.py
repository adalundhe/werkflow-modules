from __future__ import annotations
from pydantic import BaseModel
from .board_features_payload import BoardFeaturesPayload
from .boards_payload import BoardsPayload
from .field_capability_payload import FieldCapabilityPayload
from .issue_type_project_create_payload import IssueTypeProjectCreatePayload
from .notification_scheme_payload import NotificationSchemePayload
from .permission_payload_dto import PermissionPayloadDTO
from .project_payload import ProjectPayload
from .roles_capability_payload import RolesCapabilityPayload
from .scope_payload import ScopePayload
from .security_scheme_payload import SecuritySchemePayload
from .workflow_capability_payload import WorkflowCapabilityPayload


class CustomTemplateRequestDTO(BaseModel):
    boardFeatures: BoardFeaturesPayload | None = None
    boards: BoardsPayload | None = None
    field: FieldCapabilityPayload | None = None
    issueType: IssueTypeProjectCreatePayload | None = None
    notification: NotificationSchemePayload | None = None
    permissionScheme: PermissionPayloadDTO | None = None
    project: ProjectPayload | None = None
    role: RolesCapabilityPayload | None = None
    scope: ScopePayload | None = None
    security: SecuritySchemePayload | None = None
    workflow: WorkflowCapabilityPayload | None = None
