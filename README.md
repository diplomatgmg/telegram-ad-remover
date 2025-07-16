# Telegram Ad Remover

**telegram-ad-remover** is a custom Telegram bot that automatically removes advertising messages from specified channels based on defined filters.

## Features

- Automatic removal of messages containing advertising patterns (regular expressions).
- Flexible configuration of channels and filters via a configuration file.
- Event logging.
- Docker container support.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/diplomatgmg/telegram-ad-remover
cd telegram-ad-remover
```

### 2. Set up environment variables

Create a `.env` file in the project root with the following content:
```
cp .env.example .env 
```

Get your `API_ID` and `API_HASH` at [https://my.telegram.org/apps](https://my.telegram.org/apps)

Edit `.env`:
```
APP_TELETHON_API_ID=<your_api_id>
APP_TELETHON_API_HASH=<your_api_hash>
```

### 3. Configure filters and channels

Create and edit the file `src/filter_config.toml`:
```
cp src/filter_config.toml.example src/filter_config.toml
```

```toml
channel_ids = [
    -123456789,
    987654321,
]

patterns = [
    "#advertisement",
    "erid:",
]
```

- `channel_ids` — list of channel IDs where the bot will remove ads.
- `patterns` — list of patterns (regular expressions) used to identify ads.

### 4. Create a Telegram session

```bash
make create-session
```
Follow the console instructions to authorize via Telegram.

### 5. Start the bot

```bash
make up
```

## Running and Development

- To stop the container: `make down` or `make stop`

## Project Structure

- `src/main.py` — entry point, launches the client and message handler.
- `src/handlers.py` — handles new messages and ad removal.
- `src/filter_config.toml` — channels and filters configuration.
- `src/client.py` — Telegram client initialization.
- `src/create_session.py` — user session creation.
- `src/logger/` — logging setup.

## Requirements

- Python 3.13+
- Package manager [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Docker
