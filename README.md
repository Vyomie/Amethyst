# Amethyst Discord Bot

Welcome to **Amethyst**, a feature-rich and customizable bot for Discord. Amethyst offers a wide variety of commands, from utility tools and gaming mechanics to interactive chat features and music playback.

## Features

- **Adventure Game:** Engage users with an adventure game, featuring random events and rewards.
- **Slot Machine:** A gambling-inspired minigame where users can bet and win virtual currency.
- **Economy System:** Manage wallet and bank balances with commands to deposit, withdraw, and beg for virtual currency.
- **Music Playback:** Stream or play music directly from YouTube and other sources.
- **Utility Tools:** Add, rename, or delete custom emojis for your Discord server.
- **Interactive Chatbot:** Chat with the bot using AI-based responses.
- **Games:** Play Snake and Ladder and other fun games with friends.

## Commands Overview

| Command            | Alias(es)                  | Description                                                                                     |
|--------------------|----------------------------|-------------------------------------------------------------------------------------------------|
| `$ping`            |                            | Check the bot's responsiveness.                                                                |
| `$cat`             |                            | Fetch a random cat image from the internet.                                                    |
| `$adv`             | `$adventure`              | Start an adventure game.                                                                       |
| `$slots [bet]`     | `$slot`, `$Slot`           | Play a slot machine game.                                                                      |
| `$withdraw [coins]`| `$with`, `$WithDraw`       | Withdraw virtual currency from your bank account.                                              |
| `$deposit [coins]` | `$dep`, `$AddToBank`       | Deposit virtual currency into your bank account.                                               |
| `$balance [user]`  | `$bal`, `$BALANCE`         | Check the balance of a user's wallet and bank account.                                         |
| `$talk [message]`  |                            | Interact with the bot using AI responses.                                                      |
| `$play [query/url]`| `$music`, `$stream`        | Play or stream music from a URL.                                                               |
| `$shop [item] [qty]`| `$open shop`             | Buy items from the virtual shop.                                                               |

For a full list of commands and details, check the `main.py` file or the bot's command help system (`$help`).

## Prerequisites

- Python 3.8+
- Discord Bot Token: [Create one here](https://discord.com/developers/applications)
- Additional API keys for optional features (e.g., The Cat API).

## Customization

- **Adventure Events:** Modify `adv.json` to add new events.
- **Economy Items:** Update `items.json` to expand the shop offerings.
- **Emoji Management:** Use the commands to manage emojis dynamically.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request. Please ensure your changes are well-documented and tested.

## Contributors

Vyom Nishant Patel

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Discord.py** for its robust library support.
- **Chatterbot** for AI-driven chat features.
- All contributors and the open-source community.
