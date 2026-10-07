import random
from fastmcp import FastMCP

mcp = FastMCP(name="demo sever")

@mcp.tool
def roll_dice(m_dice:int=1) -> list[int]:
    return [random.randint(1,6) for _ in range(m_dice)]

@mcp.tool
def add_numbers( a: float, b: float) -> float:
    return a + b


if __name__ == "__main__":
    mcp.run()
            
            