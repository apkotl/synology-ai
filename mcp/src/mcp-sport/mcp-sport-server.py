from fastmcp import FastMCP
from typing import List

#  MCP-server initialization
mcp = FastMCP("mcp-sport-server")

# Данные
FAVORITE_SPORTS = ["Formula 1", "Biathlon", "Alpine skiing", "Soccer"]
FAVORITE_SPORTS_SUMMER = ["Formula 1", "Soccer"]
FAVORITE_SPORTS_WINTER = ["Biathlon", "Alpine skiing"]

FAVORITE_ATHLETES = [
    "Fernando Alonso",
    "Nico Hülkenberg",
    "Oscar Piastri",
    "Isack Hadjar",

    "Jakov Fak",
    "Éric Perrot",
    "Arnd Peiffer",

    "Henrik Kristoffersen",
    "Cyprien Sarrazin",
    "Lara Colturi",
    "Zrinka Ljutić",
    "Alice Robinson",

    "Xavi Hernández",
    "Andrés Iniesta",
    "Kylian Mbappé",
    "Miroslav Klose"
]

# Sports
@mcp.tool("get_sports")
async def get_sports(season: str) -> List[str]:
    """
    Returns a list of favorite sports for the season (summer, winter).
    For season use 'summer' or 'winter'. '' for all seasons.
    """
    season = season.lower()
    if "sum" in season or "лет" in season:
        return FAVORITE_SPORTS_SUMMER
    elif "win" in season or "зим" in season:
        return FAVORITE_SPORTS_WINTER
    else:
        return FAVORITE_SPORTS

# Athletes
@mcp.tool("get_athletes")
async def get_athletes() -> List[str]:
    """
    Returns a list of favorite athletes.
    """
    return FAVORITE_ATHLETES

# Find Athletes by Sport
@mcp.tool("find_athletes_by_sport")
async def find_athletes_by_sport(sport: str) -> List[str]:
    """
    Finds athletes by sport.
    Example: sport="Biathlon"
    """
    sport = sport.lower()
    if "формула" in sport or "formula" in sport:
        return ["Fernando Alonso", "Nico Hülkenberg", "Oscar Piastri", "Isack Hadjar"]
    elif "биатлон" in sport or "biathlon":
        return ["Jakov Fak", "Éric Perrot", "Arnd Peiffer"]
    #elif "лыж" in sport or "alpine ski" in sport:
    elif "лыж" in sport or "ski" in sport:
        return ["Henrik Kristoffersen", "Lara Colturi", "Zrinka Ljutić", "Alice Robinson"]
    elif "футбол" in sport or "soccer" in sport:
        return ["Xavi Hernández", "Andrés Iniesta", "Kylian Mbappé", "Miroslav Klose"]
    return []

# Find Athletes by Country
@mcp.tool("find_athletes_by_country")
async def find_athletes_by_country(country: str) -> List[str]:
    """
    Finds athletes by country.
    Use Country name or ISO 3166-1 alpha-2, alpha-3 codes.
    Example: country="New Zealand" or country="NZL" or country="NZ"
    """
    country = country.lower()
    if "испания" in country or "spain" in country or "es" in country:
        return ["Fernando Alonso", "Xavi Hernández", "Andrés Iniesta",]
    elif "германия" in country or "germany" in country or "de" in country:
        return ["Nico Hülkenberg", "Arnd Peiffer", "Miroslav Klose",]
    elif "франция" in country or "france" in country or "fr" in country:
        return ["Isack Hadjar", "Éric Perrot", "Cyprien Sarrazin", "Kylian Mbappé",]
    elif "новая зеландия" in country or "new zealand" in country or "nz" in country:
        return ["Oscar Piastri", "Alice Robinson",]
    elif "хорватия" in country or "croatia" in country or "hr" in country:
        return ["Jakov Fak", "Zrinka Ljutić",]
    elif "норвегия" in country or "norway" in country or "no" in country:
        return ["Henrik Kristoffersen",]
    elif "албания" in country or "albania" in country or "al" in country:
        return ["Lara Colturi",]
    return []


#if __name__ == "__main__":
    #mcp.run()




