# sd_telegram

[English](README_en.md) | [Русский](README.md)

A Telegram bot for generating images with Stable Diffusion, built on Aiogram 3.

## Features

-   Image generation with Stable Diffusion
-   Support for custom prompts, models, samplers, and other parameters
-   Preset configurations for quick and easy image generation
-   Integration with VK and OK for sharing images
-   Modular and extensible architecture

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/soaska/sd_telegram.git
    cd sd_telegram
    ```

2.  **Create a virtual environment and install the dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Set up the environment variables:**

    Copy the `example.env` file to `.env` and fill in the required values.

    ```bash
    cp example.env .env
    ```

    -   `API_BOT_TOKEN`: Your Telegram bot token from [BotFather](https://t.me/BotFather).
    -   `ALLOWED_USERS`: A JSON array of user IDs that are allowed to use the bot. Leave empty to allow all users.
    -   `SD_HOST`, `SD_PORT`, `SD_USERNAME`, `SD_PASSWORD`: Your Stable Diffusion API credentials.
    -   `VK_TOKEN`, `VK_ALBUM_ID`, `OK_ACCESS_TOKEN`, `OK_APPLICATION_KEY`, `OK_APPLICATION_SECRET_KEY`, `OK_GROUP_ID`: Your VK and OK API credentials.

## Usage

To run the bot, use the following command:

```bash
python bot.py
```

## Commands

-   `/start`, `/help`: Show the start message and help.
-   `/gen`: Generate an image with the current settings.
-   `/gen_custom`: Generate an image with custom settings.
-   `/skip`: Skip the current image generation.
-   `/opt`: Show the options menu.
-   `/sttngs`: Show the settings menu.
-   `/scrpts`: Show the scripts menu.

## TODO

-   [ ] Implement a more robust solution for managing the Stable Diffusion process.
-   [ ] Implement a more robust solution for handling LORA files.
-   [ ] Implement the remaining scripts (`rnd_mdl`, `rnd_smp`, `inf`).
-   [ ] Implement the remaining prompt generation strategies.
-   [ ] Implement the remaining handlers for changing parameters.
-   [ ] Add more tests.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.