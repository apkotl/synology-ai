from fastmcp import FastMCP
from typing import List

#  MCP-server initialization
mcp = FastMCP("mcp-sport-server")

# Данные
FAVORITE_CAMERAS = ["Nikon D810", "Nikon D700"]
FAVORITE_LENSES = ["14-24F2.8", "24-70F2.8", "70-200F2.8", "85F1.4"]

# Cameras
@mcp.tool("get_cameras")
async def get_cameras() -> List[str]:
    """
    Returns a list of favorite photo cameras.
    """
    return FAVORITE_CAMERAS

# Lenses
@mcp.tool("get_lenses")
async def get_lenses() -> List[str]:
    """
    Returns a list of favorite lenses.
    """
    return FAVORITE_LENSES


#if __name__ == "__main__":
    #mcp.run()




