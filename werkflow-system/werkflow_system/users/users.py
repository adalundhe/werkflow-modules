import os
import psutil
from getpass import getuser
from typing import Iterable
from pathlib import Path


class Users:

    def __init__(self) -> None:
        try:
            self._system_users = psutil.users()
        except OSError:
            self._system_users = []

        self.current_user: str = self._detect_current_user()
        self.home: Path = self._detect_home()

    @staticmethod
    def _detect_current_user() -> str:
        try:
            user = getuser()
            if user:
                return user
        except (KeyError, OSError):
            pass

        try:
            user = os.getlogin()
            if user:
                return user
        except OSError:
            pass

        env_user = os.environ.get('USER') or os.environ.get('USERNAME')
        if env_user:
            return env_user

        if hasattr(os, 'getuid'):
            return str(os.getuid())

        return 'unknown'

    @staticmethod
    def _detect_home() -> Path:
        try:
            return Path.home()
        except RuntimeError:
            fallback = os.environ.get('HOME') or os.environ.get('USERPROFILE') or os.getcwd()
            return Path(fallback)

    def list(self) -> Iterable[str]:
        for user in self._system_users:
            if not user.name.startswith('_'):
                yield user.name
