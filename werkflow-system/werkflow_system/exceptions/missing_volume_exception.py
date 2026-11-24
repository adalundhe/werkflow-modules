from typing import List


class MissingVolumeException(Exception):

    def __init__(
        self,
        supported_drives: List[str]
    ) -> None:
        supported_drive_names = '\n- '.join(supported_drives)
        prefix = '- ' if supported_drives else ''

        super().__init__(
            f'Drive does not exist or has not been mounted.\nFound drives include:\n{prefix}{supported_drive_names}'
        )
