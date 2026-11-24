from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_direct_deploy_settings import SageMakerDirectDeploySettings
from .sage_maker_emr_serverless_settings import SageMakerEmrServerlessSettings
from .sage_maker_generative_ai_settings import SageMakerGenerativeAiSettings
from .sage_maker_identity_provider_o_auth_setting import SageMakerIdentityProviderOAuthSetting
from .sage_maker_kendra_settings import SageMakerKendraSettings
from .sage_maker_model_register_settings import SageMakerModelRegisterSettings
from .sage_maker_time_series_forecasting_settings import SageMakerTimeSeriesForecastingSettings
from .sage_maker_workspace_settings import SageMakerWorkspaceSettings


class SageMakerCanvasAppSettings(BaseModel):
    TimeSeriesForecastingSettings: SageMakerTimeSeriesForecastingSettings | None = None
    ModelRegisterSettings: SageMakerModelRegisterSettings | None = None
    WorkspaceSettings: SageMakerWorkspaceSettings | None = None
    IdentityProviderOAuthSettings: list[SageMakerIdentityProviderOAuthSetting] | None = None
    DirectDeploySettings: SageMakerDirectDeploySettings | None = None
    KendraSettings: SageMakerKendraSettings | None = None
    GenerativeAiSettings: SageMakerGenerativeAiSettings | None = None
    EmrServerlessSettings: SageMakerEmrServerlessSettings | None = None
