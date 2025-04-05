import sys
import datetime
from enum import Enum
from typing import TextIO, Optional, TypeAlias


LogLevel_alias : TypeAlias = "LogLevel"
Logger_alias : TypeAlias = "Logger"


class LogLevel(Enum):
    DEBUG = (0, '\033[37m')     # White
    INFO = (1, '\033[32m')      # Green
    WARNING = (2, '\033[33m')   # Yellow
    ERROR = (3, '\033[31m')     # Red
    CRITICAL = (4, '\033[35m')  # Magenta

    def __init__(self, level: int, color: str):
        self.level = level
        self.color = color

class Logger:
    RESET_COLOR = '\033[0m'

    def __init__(self, 
                 min_level: LogLevel = LogLevel.DEBUG,
                 output_file: Optional[str] = None,
                 use_colors: bool = True):
        self.min_level = min_level
        self.use_colors = use_colors and output_file is None  # Colors only for terminal
        self.output: TextIO = open(output_file, 'a') if output_file else sys.stdout

    def _log(self, level: LogLevel, message: str, *args, **kwargs):
        if level.level < self.min_level.level:
            return

        # Format message with args and kwargs
        if args or kwargs:
            message = message.format(*args, **kwargs)

        # Create timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Build log message
        log_message = f"[{timestamp}] {level.name}: {message}"
        
        # Add colors if enabled and writing to terminal
        if self.use_colors and self.output == sys.stdout:
            log_message = f"{level.color}{log_message}{self.RESET_COLOR}"

        # Write log message
        self.output.write(log_message + '\n')
        self.output.flush()

    def debug(self, message: str, *args, **kwargs):
        self._log(LogLevel.DEBUG, message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self._log(LogLevel.INFO, message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        self._log(LogLevel.WARNING, message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        self._log(LogLevel.ERROR, message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs):
        self._log(LogLevel.CRITICAL, message, *args, **kwargs)

    def __del__(self):
        if self.output != sys.stdout:
            self.output.close()

# Example usage:
if __name__ == "__main__":
    # Terminal logger with colors
    console_logger = Logger(min_level=LogLevel.DEBUG, use_colors=True)
    
    # File logger
    file_logger = Logger(min_level=LogLevel.INFO, output_file="app.log")
    
    # Example logs
    console_logger.debug("This is a debug message")
    console_logger.info("User {} logged in successfully", "John")
    console_logger.warning("System resources at {:.1f}%", 85.5)
    console_logger.error("Failed to connect to database: {error}", error="Connection timeout")
    console_logger.critical("System shutdown initiated")
    
    # Same messages to file
    file_logger.debug("This is a debug message")
    file_logger.info("User {} logged in successfully", "John")
    file_logger.warning("System resources at {:.1f}%", 85.5)
    file_logger.error("Failed to connect to database: {error}", error="Connection timeout")
    file_logger.critical("System shutdown initiated")
