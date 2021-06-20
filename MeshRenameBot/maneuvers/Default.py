from abc import ABC, abstractmethod
from pyrogram import Client
from pyrogram.types import Message


class DefaultManeuver(ABC):
    def __init__(self, client: Client, media_message: Message, cmd_message: Message) -> None:
        self._client = client
        self._media_message = media_message
        self._cmd_message = cmd_message
        self._sender_id = cmd_message.from_user.id
        self._chat_id = cmd_message.chat.id
        self._unique_id = 0

        self._canceled = False  # Track the cancel status
        self._halt = False  # Track if the maneuver is halted [not implemented]
    
    @property
    def sender_id(self) -> int:
        return self._sender_id

    @property
    def chat_id(self) -> int:
        return self._chat_id

    @abstractmethod
    async def execute(self) -> None:
        raise NotImplementedError("Not implemented the method execute from the calling class.")
    
    def cancel(self) -> None:
        self._canceled = True
    
    def halt(self) -> None:
        self._halt = True

    @property
    def is_halted(self) -> bool:
        return self._halt

    @property
    def is_canceled(self) -> bool:
        return self._canceled
