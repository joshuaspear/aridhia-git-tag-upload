import os
import logging
from subprocess import call
import argparse
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class ApiCommunicator:

    def __init__(self, path_to_file, token, recurse=True):
        self.path_to_file = path_to_file
        self.token = token
        self.path_is_file = os.path.isfile(self.path_to_file)
        self.path_is_dir = os.path.isdir(self.path_to_file)
        logging.info("Using path {}".format(path_to_file))
        logging.debug("self.path_is_dir: {}".format(self.path_is_dir))
        if not self.path_is_file and not self.path_is_dir:
            logging.error("Path must be a valid file or directory")
            raise ValueError
        if self.path_is_dir and recurse:
            logging.info("Supplied path is a directory. Recursively uploading contents. Set recurs as False to override")
            self.recurs = True
        else:
            self.recurs = False

    def upload_file(self):
        call_list = ["azcopy", "copy", self.path_to_file, self.token]
        if self.recurs:
            call_list.append("--recursive=true")
        logging.debug("Subprocess command: {}".format(call_list))
        logging.info("Running subprocess to upload files via azcopy")
        call(call_list)
        return True


def main(path_to_file, recurse):
    logging.info("Building ApiCommunicator")
    token = json.load(open(".aridhia_secret.json"))["az_copy_token"]
    api_com = ApiCommunicator(path_to_file, token, recurse)
    logging.info("Building uploading file")
    api_com.upload_file()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path_to_file", help="path to the file or directory to be uploaded")
    parser.add_argument("--recurse", default=True, help="toggle to recursively upload a directory")
    parser.add_argument("--suppress_info", default=False, help="if set to true logging will be set to error level")
    args = parser.parse_args()
    if args.suppress_info:
        logger.setLevel(logging.ERROR)
    main(args.path_to_file, args.recurse)
