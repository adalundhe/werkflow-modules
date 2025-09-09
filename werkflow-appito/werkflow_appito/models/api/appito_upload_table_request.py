from pydantic import BaseModel, StrictStr, StrictBool
from werkflow_appito.models.shared.appito_credentials import AppitoCredentials
from werkflow_http.request import File

class AppitoUploadTableRequest(BaseModel):
    appito_domain: StrictStr
    appito_csv_file: StrictStr | File
    appito_project: StrictStr
    appito_table_name: StrictStr
    appito_time_period: StrictStr = "current"
    appito_environment_id: StrictStr | None = None
    appito_action: StrictStr | None = None
    appito_force: StrictBool | None = None
    appito_credentials: AppitoCredentials | None = None

    