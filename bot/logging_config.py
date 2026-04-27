import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # ADD encoding='utf-8' HERE!
        file_handler = logging.FileHandler("bot.log", encoding='utf-8') 
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger