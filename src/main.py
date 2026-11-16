import logging

from extract import extract_users
from transform import transform_users
from database import load_users


logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)


def run_pipeline():

    logging.info(
        "Pipeline started"
    )

    try:

        raw_users = extract_users()

        logging.info(
            "Extracted %s records",
            len(raw_users)
        )

        clean_users = transform_users(
            raw_users
        )

        logging.info(
            "Validated %s records",
            len(clean_users)
        )

        load_users(clean_users)

        logging.info(
            "Pipeline completed successfully"
        )

    except Exception:

        logging.exception(
            "Pipeline failed"
        )

        raise


if __name__ == "__main__":

    run_pipeline()