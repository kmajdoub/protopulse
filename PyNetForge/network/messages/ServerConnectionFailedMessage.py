from typing import TYPE_CHECKING

from PyNetForge.network.messages.Message import Message

if TYPE_CHECKING:
    from PyNetForge.network.ServerConnection import ServerConnection


class ServerConnectionFailedMessage(Message):

    _failedConnection: "ServerConnection"

    _errorMessage: str

    def __init__(self, failedConnection: "ServerConnection", errorMessage: str):
        super().__init__()
        self._errorMessage = errorMessage
        self._failedConnection = failedConnection

    @property
    def failedConnection(self) -> "ServerConnection":
        return self._failedConnection

    @property
    def errorMessage(self) -> str:
        return self._errorMessage