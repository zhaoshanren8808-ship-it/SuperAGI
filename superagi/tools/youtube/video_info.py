from typing import Type
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class VideoInfoInput(BaseModel):
    video_id: str = Field(..., description="The YouTube video ID")


class VideoInfoTool(BaseTool):
    name: str = "Get YouTube Video Info"
    args_schema: Type[BaseModel] = VideoInfoInput
    description: str = "Retrieve detailed information about a YouTube video including statistics"

    def _execute(self, video_id: str):
        """
        Get video information.
        
        Args:
            video_id: The YouTube video ID
        
        Returns:
            Video details including title, description, statistics
        """
        api_key = self.get_tool_config("YOUTUBE_API_KEY")
        if not api_key:
            return "Error: YOUTUBE_API_KEY is not configured."
        
        base_url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            "part": "snippet,statistics,contentDetails",
            "id": video_id,
            "key": api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            items = data.get("items", [])
            if not items:
                return f"No video found with ID: {video_id}"
            
            video = items[0]
            snippet = video.get("snippet", {})
            stats = video.get("statistics", {})
            
            result = f"YouTube Video Information:\n\n"
            result += f"**Title**: {snippet.get('title', 'N/A')}\n"
            result += f"**Channel**: {snippet.get('channelTitle', 'N/A')}\n"
            result += f"**Published**: {snippet.get('publishedAt', 'N/A')}\n"
            result += f"**Duration**: {video.get('contentDetails', {}).get('duration', 'N/A')}\n\n"
            result += f"**Statistics**:\n"
            result += f"- Views: {stats.get('viewCount', 'N/A')}\n"
            result += f"- Likes: {stats.get('likeCount', 'N/A')}\n"
            result += f"- Comments: {stats.get('commentCount', 'N/A')}\n\n"
            result += f"**Description**:\n{snippet.get('description', 'N/A')[:500]}...\n\n"
            result += f"**URL**: https://www.youtube.com/watch?v={video_id}"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error getting video info: {str(e)}"