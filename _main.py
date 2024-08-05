import argparse
import logging
import logging.config
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "src"))
logging.config.fileConfig("log.ini", disable_existing_loggers=False)
# logging.disable()


logger = logging.getLogger()


def main():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )

    parser.add_argument("name")

    args = parser.parse_args()


if __name__ == "__main__":
    logging.info("MAIN START")  #  extra={"key": "value"}

    main()

    logging.info("MAIN CLOSE")
