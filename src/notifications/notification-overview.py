from loguru import logger

import notification

if __name__ == '__main__':
    logger.info('Notifying overview weekly')

    try:
        with open("../templates/TEMP_OVERVIEW_WEEKLY.j2", "r", encoding="utf-8") as stream:
            content = stream.read()
        notification.send_message(message=content)
        logger.info("Already sent notification")
    except Exception as e:
        logger.error("Notifying overview error: {}", e)
