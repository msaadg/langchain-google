"""Base class for Gmail tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

from langchain_core.tools import BaseTool
from pydantic import Field

from langchain_google_community.gmail.utils import build_gmail_service

if TYPE_CHECKING:
    # This is for linting and IDE typehints
    from googleapiclient.discovery import Resource  # type: ignore[import]
else:
    try:
        # We do this so pydantic can resolve the types when instantiating
        from googleapiclient.discovery import Resource
    except ImportError:
        pass


class GmailBaseTool(BaseTool):
    """Base class for Gmail tools."""

    api_resource: Resource = Field(default_factory=build_gmail_service)

    @classmethod
    def from_api_resource(cls, api_resource: Resource) -> "GmailBaseTool":
        """Create a tool from an api resource.

        Args:
            api_resource: The api resource to use.

        Returns:
            A tool.
        """
        return cls(service=api_resource)  # type: ignore[call-arg]
