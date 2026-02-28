from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class ChannelInfoInput(BaseModel):
    channel_id: str = Field(..., description="The YouTube channel ID")


class ChannelInfoTool(BaseTool):
    name: str = "Get YouTube Channel Info"
    args_schema: Type[BaseModel] = ChannelInfoInput
    description: str = "Retrieve information about a YouTube channel"

    def _execute(self, channel_id: str):
        """
        Get channel information.
        
        Args:
            channel_id: The YouTube channel ID
        
        Returns:
            Channel details including name, description, statistics
        """
        api_key = self.get_tool_config("YOUTUBE_API_KEY")
        if not api_key:
            return "Error: YOUTUBE_API_KEY is not configured."
        
        base_url = "https://www.googleapis.com/youtube/v3/channels"
        params = {
            "part": "snippet,statistics,contentDetails",
            "id": channel_id,
            "key": api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            items = data.get("items", [])
            if not items:
                return f"No channel found with ID: {channel_id}"
            
            channel = items[0]
            snippet = channel.get("snippet", {})
            stats = channel.get("statistics", {})
            
            result = f"YouTube Channel Information:\n\n"
            result += f"**Title**: {snippet.get('title', 'N/A')}\n"
            result += f"**Custom URL**: {snippet.get('customUrl', 'N/A')}\n"
            result += f"**Country**: {snippet.get('country', 'N/A')}\n"
            result += f"**Created**: {snippet.get('publishedAt', 'N/A')}\n\n"
            result += f"**Statistics**:\n"
            result += f"- Subscribers: {stats.get('subscriberCount', 'N/A')}\n"
            result += f"- Total Views: {stats.get('viewCount', 'N/A')}\n"
            result += f"- Video Count: {stats.get('videoCount', 'N/A')}\n\n"
            result += f"**Description**:\n{snippet.get('description', 'N/A')[:500]}...\n\n"
            result += f"**URL**: https://www.youtube.com/channel/{channel_id}"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error getting channel info: {str(e)}"