from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_aiml_options_input import OpenSearchAIMLOptionsInput
from .open_search_advanced_security_options_input import OpenSearchAdvancedSecurityOptionsInput
from .open_search_auto_tune_options_input import OpenSearchAutoTuneOptionsInput
from .open_search_automated_snapshot_pause_request_options import OpenSearchAutomatedSnapshotPauseRequestOptions
from .open_search_cluster_config import OpenSearchClusterConfig
from .open_search_cognito_options import OpenSearchCognitoOptions
from .open_search_deployment_strategy_options import OpenSearchDeploymentStrategyOptions
from .open_search_domain_endpoint_options import OpenSearchDomainEndpointOptions
from .open_search_ebs_options import OpenSearchEBSOptions
from .open_search_encryption_at_rest_options import OpenSearchEncryptionAtRestOptions
from .open_search_identity_center_options_input import OpenSearchIdentityCenterOptionsInput
from .open_search_log_publishing_option import OpenSearchLogPublishingOption
from .open_search_node_to_node_encryption_options import OpenSearchNodeToNodeEncryptionOptions
from .open_search_off_peak_window_options import OpenSearchOffPeakWindowOptions
from .open_search_snapshot_options import OpenSearchSnapshotOptions
from .open_search_software_update_options import OpenSearchSoftwareUpdateOptions
from .open_search_tag import OpenSearchTag
from .open_search_vpc_options import OpenSearchVPCOptions


class OpenSearchCreateDomainRequest(BaseModel):
    DomainName: StrictStr
    EngineVersion: StrictStr | None = None
    ClusterConfig: OpenSearchClusterConfig | None = None
    EBSOptions: OpenSearchEBSOptions | None = None
    AccessPolicies: StrictStr | None = None
    IPAddressType: Literal['ipv4', 'dualstack'] | None = None
    SnapshotOptions: OpenSearchSnapshotOptions | None = None
    VPCOptions: OpenSearchVPCOptions | None = None
    CognitoOptions: OpenSearchCognitoOptions | None = None
    EncryptionAtRestOptions: OpenSearchEncryptionAtRestOptions | None = None
    NodeToNodeEncryptionOptions: OpenSearchNodeToNodeEncryptionOptions | None = None
    AdvancedOptions: dict[StrictStr, StrictStr] | None = None
    LogPublishingOptions: dict[Literal['INDEX_SLOW_LOGS', 'SEARCH_SLOW_LOGS', 'ES_APPLICATION_LOGS', 'AUDIT_LOGS'], OpenSearchLogPublishingOption] | None = None
    DomainEndpointOptions: OpenSearchDomainEndpointOptions | None = None
    AdvancedSecurityOptions: OpenSearchAdvancedSecurityOptionsInput | None = None
    IdentityCenterOptions: OpenSearchIdentityCenterOptionsInput | None = None
    TagList: list[OpenSearchTag] | None = None
    AutoTuneOptions: OpenSearchAutoTuneOptionsInput | None = None
    OffPeakWindowOptions: OpenSearchOffPeakWindowOptions | None = None
    SoftwareUpdateOptions: OpenSearchSoftwareUpdateOptions | None = None
    AIMLOptions: OpenSearchAIMLOptionsInput | None = None
    DeploymentStrategyOptions: OpenSearchDeploymentStrategyOptions | None = None
    AutomatedSnapshotPauseOptions: OpenSearchAutomatedSnapshotPauseRequestOptions | None = None
    UseCase: Literal['SEARCH', 'VECTOR', 'OBSERVABILITY', 'MIXED'] | None = None
    EngineMode: Literal['GENERAL', 'OPTIMIZED'] | None = None
