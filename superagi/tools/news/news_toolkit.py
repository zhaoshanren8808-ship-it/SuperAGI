from abc import ABC
from typing import List
from superagi.tools.base_tool import BaseTool, BaseToolkit, ToolConfiguration
from superagi.tools.news.get_top_headlines import GetTopHeadlinesTool
from superagi.tools.news.search_news import SearchNewsTool
from superagi.types.key_type import ToolConfigKeyType


class NewsToolkit(BaseToolkit, ABC):
    name: str = "News Toolkit"
    description: str = "News Toolkit provides tools to interact with NewsAPI for retrieving and searching news articles from various sources worldwide."

    def get_tools(self) -> List[BaseTool]:
        return [
            GetTopHeadlinesTool(),
            SearchNewsTool()
        ]

    def get_env_keys(self) -> List[ToolConfiguration]:
        return [
            ToolConfiguration(key="NEWS_API_KEY", key_type=ToolConfigKeyType.STRING, is_required=True, is_secret=True)
        ]