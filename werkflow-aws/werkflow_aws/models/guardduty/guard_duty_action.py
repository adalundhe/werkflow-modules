from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_aws_api_call_action import GuardDutyAwsApiCallAction
from .guard_duty_dns_request_action import GuardDutyDnsRequestAction
from .guard_duty_kubernetes_api_call_action import GuardDutyKubernetesApiCallAction
from .guard_duty_kubernetes_permission_checked_details import GuardDutyKubernetesPermissionCheckedDetails
from .guard_duty_kubernetes_role_binding_details import GuardDutyKubernetesRoleBindingDetails
from .guard_duty_kubernetes_role_details import GuardDutyKubernetesRoleDetails
from .guard_duty_network_connection_action import GuardDutyNetworkConnectionAction
from .guard_duty_port_probe_action import GuardDutyPortProbeAction
from .guard_duty_rds_login_attempt_action import GuardDutyRdsLoginAttemptAction


class GuardDutyAction(BaseModel):
    ActionType: StrictStr | None = None
    AwsApiCallAction: GuardDutyAwsApiCallAction | None = None
    DnsRequestAction: GuardDutyDnsRequestAction | None = None
    NetworkConnectionAction: GuardDutyNetworkConnectionAction | None = None
    PortProbeAction: GuardDutyPortProbeAction | None = None
    KubernetesApiCallAction: GuardDutyKubernetesApiCallAction | None = None
    KubernetesPermissionCheckedDetails: GuardDutyKubernetesPermissionCheckedDetails | None = None
    KubernetesRoleBindingDetails: GuardDutyKubernetesRoleBindingDetails | None = None
    KubernetesRoleDetails: GuardDutyKubernetesRoleDetails | None = None
    RdsLoginAttemptAction: GuardDutyRdsLoginAttemptAction | None = None
