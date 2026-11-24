from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_serverless_v2_features_support import DocumentDBServerlessV2FeaturesSupport
from .document_db_upgrade_target import DocumentDBUpgradeTarget


class DocumentDBDBEngineVersion(BaseModel):
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    DBParameterGroupFamily: StrictStr | None = None
    DBEngineDescription: StrictStr | None = None
    DBEngineVersionDescription: StrictStr | None = None
    ValidUpgradeTarget: list[DocumentDBUpgradeTarget] | None = None
    ExportableLogTypes: list[StrictStr] | None = None
    SupportsLogExportsToCloudwatchLogs: StrictBool | None = None
    SupportedCACertificateIdentifiers: list[StrictStr] | None = None
    SupportsCertificateRotationWithoutRestart: StrictBool | None = None
    ServerlessV2FeaturesSupport: DocumentDBServerlessV2FeaturesSupport | None = None
