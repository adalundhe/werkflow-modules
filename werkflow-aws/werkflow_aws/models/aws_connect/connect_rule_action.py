from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_assign_contact_category_action_definition import ConnectAssignContactCategoryActionDefinition
from .connect_assign_sla_action_definition import ConnectAssignSlaActionDefinition
from .connect_create_case_action_definition import ConnectCreateCaseActionDefinition
from .connect_end_associated_emails_action_definition import ConnectEndAssociatedEmailsActionDefinition
from .connect_end_associated_tasks_action_definition import ConnectEndAssociatedTasksActionDefinition
from .connect_event_bridge_action_definition import ConnectEventBridgeActionDefinition
from .connect_extract_information_action_definition import ConnectExtractInformationActionDefinition
from .connect_send_in_app_notification_action_definition import ConnectSendInAppNotificationActionDefinition
from .connect_send_notification_action_definition import ConnectSendNotificationActionDefinition
from .connect_submit_auto_evaluation_action_definition import ConnectSubmitAutoEvaluationActionDefinition
from .connect_task_action_definition import ConnectTaskActionDefinition
from .connect_update_case_action_definition import ConnectUpdateCaseActionDefinition


class ConnectRuleAction(BaseModel):
    ActionType: StrictStr | None = None
    TaskAction: ConnectTaskActionDefinition | None = None
    EventBridgeAction: ConnectEventBridgeActionDefinition | None = None
    AssignContactCategoryAction: ConnectAssignContactCategoryActionDefinition | None = None
    SendNotificationAction: ConnectSendNotificationActionDefinition | None = None
    CreateCaseAction: ConnectCreateCaseActionDefinition | None = None
    UpdateCaseAction: ConnectUpdateCaseActionDefinition | None = None
    AssignSlaAction: ConnectAssignSlaActionDefinition | None = None
    EndAssociatedTasksAction: ConnectEndAssociatedTasksActionDefinition | None = None
    EndAssociatedEmailsAction: ConnectEndAssociatedEmailsActionDefinition | None = None
    SubmitAutoEvaluationAction: ConnectSubmitAutoEvaluationActionDefinition | None = None
    ExtractInformationAction: ConnectExtractInformationActionDefinition | None = None
    SendInAppNotificationAction: ConnectSendInAppNotificationActionDefinition | None = None
