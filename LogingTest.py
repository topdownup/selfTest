import logging
import logging.config

conffile = "conf/log.conf"
config = logging.config.fileConfig(conffile)
logger = logging.getLogger("root")
logger.info("root!")

logger = logging.getLogger("xzc")
logger.error("xzc!")
