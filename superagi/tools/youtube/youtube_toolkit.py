from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from superagi.tools.youtube.video_search import VideoSearchTool
from superagi.tools.youtube.video_info import VideoInfoTool
from superagi.tools.youtube.channel_info import ChannelInfoTool
from superagi.tools.youtube.video_comments import VideoCommentsTool
from superagi.types.key_type import ToolConfigKeyType


class YoutubeToolkit(BaseToolkit, ABC):
    name: str = "YouTube Toolkit"
    description: str = "YouTube Toolkit enables interaction with YouTube's API for video search, summarization, comment retrieval, and channel information."

    def get_tools(self) -> List[BaseTool]:
        return [
            VideoSearchTool(),
            VideoInfoTool(),
            ChannelInfoTool(),
            VideoCommentsTool()
        ]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key="YOUTUBE_API_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True)
        ]