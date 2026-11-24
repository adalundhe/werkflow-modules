from __future__ import annotations
from pydantic import BaseModel
from .open_search_aiml_options_status import OpenSearchAIMLOptionsStatus
from .open_search_access_policies_status import OpenSearchAccessPoliciesStatus
from .open_search_advanced_options_status import OpenSearchAdvancedOptionsStatus
from .open_search_advanced_security_options_status import OpenSearchAdvancedSecurityOptionsStatus
from .open_search_auto_tune_options_status import OpenSearchAutoTuneOptionsStatus
from .open_search_automated_snapshot_pause_options_status import OpenSearchAutomatedSnapshotPauseOptionsStatus
from .open_search_change_progress_details import OpenSearchChangeProgressDetails
from .open_search_cluster_config_status import OpenSearchClusterConfigStatus
from .open_search_cognito_options_status import OpenSearchCognitoOptionsStatus
from .open_search_deployment_strategy_options_status import OpenSearchDeploymentStrategyOptionsStatus
from .open_search_domain_endpoint_options_status import OpenSearchDomainEndpointOptionsStatus
from .open_search_ebs_options_status import OpenSearchEBSOptionsStatus
from .open_search_encryption_at_rest_options_status import OpenSearchEncryptionAtRestOptionsStatus
from .open_search_engine_mode_status import OpenSearchEngineModeStatus
from .open_search_ip_address_type_status import OpenSearchIPAddressTypeStatus
from .open_search_identity_center_options_status import OpenSearchIdentityCenterOptionsStatus
from .open_search_log_publishing_options_status import OpenSearchLogPublishingOptionsStatus
from .open_search_modifying_properties import OpenSearchModifyingProperties
from .open_search_node_to_node_encryption_options_status import OpenSearchNodeToNodeEncryptionOptionsStatus
from .open_search_off_peak_window_options_status import OpenSearchOffPeakWindowOptionsStatus
from .open_search_snapshot_options_status import OpenSearchSnapshotOptionsStatus
from .open_search_software_update_options_status import OpenSearchSoftwareUpdateOptionsStatus
from .open_search_use_case_status import OpenSearchUseCaseStatus
from .open_search_vpc_derived_info_status import OpenSearchVPCDerivedInfoStatus
from .open_search_version_status import OpenSearchVersionStatus


class OpenSearchDomainConfig(BaseModel):
    EngineVersion: OpenSearchVersionStatus | None = None
    ClusterConfig: OpenSearchClusterConfigStatus | None = None
    EBSOptions: OpenSearchEBSOptionsStatus | None = None
    AccessPolicies: OpenSearchAccessPoliciesStatus | None = None
    IPAddressType: OpenSearchIPAddressTypeStatus | None = None
    SnapshotOptions: OpenSearchSnapshotOptionsStatus | None = None
    VPCOptions: OpenSearchVPCDerivedInfoStatus | None = None
    CognitoOptions: OpenSearchCognitoOptionsStatus | None = None
    EncryptionAtRestOptions: OpenSearchEncryptionAtRestOptionsStatus | None = None
    NodeToNodeEncryptionOptions: OpenSearchNodeToNodeEncryptionOptionsStatus | None = None
    AdvancedOptions: OpenSearchAdvancedOptionsStatus | None = None
    LogPublishingOptions: OpenSearchLogPublishingOptionsStatus | None = None
    DomainEndpointOptions: OpenSearchDomainEndpointOptionsStatus | None = None
    AdvancedSecurityOptions: OpenSearchAdvancedSecurityOptionsStatus | None = None
    IdentityCenterOptions: OpenSearchIdentityCenterOptionsStatus | None = None
    AutoTuneOptions: OpenSearchAutoTuneOptionsStatus | None = None
    ChangeProgressDetails: OpenSearchChangeProgressDetails | None = None
    OffPeakWindowOptions: OpenSearchOffPeakWindowOptionsStatus | None = None
    SoftwareUpdateOptions: OpenSearchSoftwareUpdateOptionsStatus | None = None
    ModifyingProperties: list[OpenSearchModifyingProperties] | None = None
    AIMLOptions: OpenSearchAIMLOptionsStatus | None = None
    DeploymentStrategyOptions: OpenSearchDeploymentStrategyOptionsStatus | None = None
    AutomatedSnapshotPauseOptions: OpenSearchAutomatedSnapshotPauseOptionsStatus | None = None
    UseCase: OpenSearchUseCaseStatus | None = None
    EngineMode: OpenSearchEngineModeStatus | None = None
