from typing import Type, Optional
from pydantic import BaseModel, Field
from superagi.tools.base_tool import BaseTool
import requests


class VideoCommentsInput(BaseModel):
    video_id: str = Field(..., description="The YouTube video ID")
    max_results: Optional[int] = Field(20, description="Maximum number of comments to retrieve")


class VideoCommentsTool(BaseTool):
    name: str = "Get YouTube Video Comments"
    args_schema: Type[BaseModel] = VideoCommentsInput
    description: str = "Retrieve comments from a YouTube video"

    def _execute(self, video_id: str, max_results: Optional[int] = 20):
        """
        Get video comments.
        
        Args:
            video_id: The YouTube video ID
            max_results: Maximum comments to retrieve
        
        Returns:
            List of comments with author and text
        """
        api_key = self.get_tool_config("YOUTUBE_API_KEY")
        if not api_key:
            return "Error: YOUTUBE_API_KEY is not configured."
        
        # First, get the comment thread ID for the video
        base_url = "https://www.googleapis.com/youtube/v3/commentThreads"
        params = {
            "part": "snippet",
            "videoId": video_id,
            "maxResults": max_results,
            "order": "relevance",
            "key": api_key
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            items = data.get("items", [])
            if not items:
                return f"No comments found for video: {video_id}"
            
            result = f"YouTube Video Comments:\n\n"
            for i, item in enumerate(items, 1):
                comment = item.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
                author = comment.get("authorDisplayName", "Anonymous")
                text = comment.get("textDisplay", "")
                likes = comment.get("likeCount", 0)
                
                result += f"{i}. **{author}** ({likes} likes)\n"
                result += f"   {text[:200]}{'...' if len(text) > 200 else ''}\n\n"
            
            return result
            
        except requests.exceptions.RequestException as e:
            return f"Error getting comments: {str(e)}"