# Using the Python 3.11 slim image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install the UV package manager
RUN pip install uv 

# Copying project files
#COPY src/pyproject.toml .
#COPY src/uv.lock .
#COPY src/mcp-photo/ mcp-photo/
#COPY src/mcp-sport/ mcp-sport/
COPY src/ .


# Installing dependencies using uv
RUN uv sync --frozen

# Specify the ports used by the application (overridden in docker-compose)
#EXPOSE 3001 3002 3003

# The default command is overridden in docker-compose
CMD ["uv", "run", "fastmcp"]
