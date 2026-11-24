from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .open_search_aiml_options_output import OpenSearchAIMLOptionsOutput
from .open_search_advanced_security_options import OpenSearchAdvancedSecurityOptions
from .open_search_auto_tune_options_output import OpenSearchAutoTuneOptionsOutput
from .open_search_automated_snapshot_pause_options import OpenSearchAutomatedSnapshotPauseOptions
from .open_search_change_progress_details import OpenSearchChangeProgressDetails
from .open_search_cluster_config import OpenSearchClusterConfig
from .open_search_cognito_options import OpenSearchCognitoOptions
from .open_search_deployment_strategy_options import OpenSearchDeploymentStrategyOptions
from .open_search_domain_endpoint_options import OpenSearchDomainEndpointOptions
from .open_search_ebs_options import OpenSearchEBSOptions
from .open_search_encryption_at_rest_options import OpenSearchEncryptionAtRestOptions
from .open_search_identity_center_options import OpenSearchIdentityCenterOptions
from .open_search_log_publishing_option import OpenSearchLogPublishingOption
from .open_search_modifying_properties import OpenSearchModifyingProperties
from .open_search_node_to_node_encryption_options import OpenSearchNodeToNodeEncryptionOptions
from .open_search_off_peak_window_options import OpenSearchOffPeakWindowOptions
from .open_search_service_software_options import OpenSearchServiceSoftwareOptions
from .open_search_snapshot_options import OpenSearchSnapshotOptions
from .open_search_software_update_options import OpenSearchSoftwareUpdateOptions
from .open_search_vpc_derived_info import OpenSearchVPCDerivedInfo


class OpenSearchDomainStatus(BaseModel):
    DomainId: StrictStr | None = None
    DomainName: StrictStr | None = None
    ARN: StrictStr | None = None
    Created: StrictBool | None = None
    Deleted: StrictBool | None = None
    Endpoint: StrictStr | None = None
    EndpointV2: StrictStr | None = None
    Endpoints: dict[StrictStr, StrictStr] | None = None
    DomainEndpointV2HostedZoneId: StrictStr | None = None
    Processing: StrictBool | None = None
    UpgradeProcessing: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    ClusterConfig: OpenSearchClusterConfig | None = None
    EBSOptions: OpenSearchEBSOptions | None = None
    AccessPolicies: StrictStr | None = None
    IPAddressType: StrictStr | None = None
    SnapshotOptions: OpenSearchSnapshotOptions | None = None
    VPCOptions: OpenSearchVPCDerivedInfo | None = None
    CognitoOptions: OpenSearchCognitoOptions | None = None
    EncryptionAtRestOptions: OpenSearchEncryptionAtRestOptions | None = None
    NodeToNodeEncryptionOptions: OpenSearchNodeToNodeEncryptionOptions | None = None
    AdvancedOptions: dict[StrictStr, StrictStr] | None = None
    LogPublishingOptions: dict[StrictStr, OpenSearchLogPublishingOption] | None = None
    ServiceSoftwareOptions: OpenSearchServiceSoftwareOptions | None = None
    DomainEndpointOptions: OpenSearchDomainEndpointOptions | None = None
    AdvancedSecurityOptions: OpenSearchAdvancedSecurityOptions | None = None
    IdentityCenterOptions: OpenSearchIdentityCenterOptions | None = None
    AutoTuneOptions: OpenSearchAutoTuneOptionsOutput | None = None
    ChangeProgressDetails: OpenSearchChangeProgressDetails | None = None
    OffPeakWindowOptions: OpenSearchOffPeakWindowOptions | None = None
    SoftwareUpdateOptions: OpenSearchSoftwareUpdateOptions | None = None
    DomainProcessingStatus: StrictStr | None = None
    ModifyingProperties: list[OpenSearchModifyingProperties] | None = None
    AIMLOptions: OpenSearchAIMLOptionsOutput | None = None
    DeploymentStrategyOptions: OpenSearchDeploymentStrategyOptions | None = None
    AutomatedSnapshotPauseOptions: OpenSearchAutomatedSnapshotPauseOptions | None = None
    UseCase: StrictStr | None = None
    EngineMode: StrictStr | None = None
