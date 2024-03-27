<br/>
<p align="center">
  <a href="https://github.com/Corner324/TelegramPredictions">
    <img src="https://i.imgur.com/mTPZfH1.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Telegram Bot Prediction</h3>

  <p align="center">
    A telegram bot that implements parsing of pages with predictions and their further planned publication in selected chats.
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/Corner324/TelegramPredictions/total) ![Contributors](https://img.shields.io/github/contributors/Corner324/TelegramPredictions?color=dark-green) ![Issues](https://img.shields.io/github/issues/Corner324/TelegramPredictions) ![License](https://img.shields.io/github/license/Corner324/TelegramPredictions) 


**Telegram Bot for Predictions**

This project is a Telegram bot designed to parse prediction pages and schedule their publication in specified chats.

### Features
- Parses prediction data from specified sources.
- Schedules the publication of predictions at predetermined times.
- Logs events and errors for monitoring and debugging purposes.

### Usage
1. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

2. Obtain a Telegram API token from BotFather and set it in the `config.py` file.

3. Adjust the target time for prediction publication and other settings in the `config.py` file as needed.

4. Run the bot:
   ```bash
   python main.py
   ```

### Dependencies
- `aiogram`: Telegram Bot API framework for Python.
- `asyncio`: Asynchronous I/O library for concurrent code execution.
- `datetime`: Module for manipulating dates and times.
- `utils`: Custom utility functions for time manipulation.
- `logger`: Custom logger module for handling bot logs.

### Configuration
- `config.py`: Contains configuration variables such as API token, target publication time, and chat IDs.

### File Structure
- `main.py`: Entry point of the Telegram bot.
- `config.py`: Configuration file for storing API token and other settings.
- `logger.py`: Module for logging events and errors.
- `prediction.py`: Module for parsing prediction data from web pages.
- `utils`: Directory containing utility functions for date and time manipulation.


### Credits
- Developed by [Corner324](https://github.com/Corner324).
  
### License
This project is licensed under the [MIT License](https://github.com/Corner324/Bobby-LEO/blob/main/LICENSE).

### Disclaimer
This bot is provided as-is without any warranty. Use it at your own risk.

For any questions or issues, please contact the project maintainers.

