import argparse
import os

from analysis.Analyse import DockerImage
from parser.file_contents import FileManagement
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', help="search directory")
parser.add_argument('-r', '--repo', help="repo org/name")
parser.add_argument('-v', '--repoversion', help="repo version")
parser.add_argument('-t', '--testing', help="run as testing", nargs="?", const="tangent")


OUTPUT_DIR = "./data/"
TEST_OPTIONS = {
    'tangent': {
        'dir': './examples/tangent/',
        'repo': 'brombaut/tangent',
        'repoversion': '0.0.0'
    },
    'neuralint': {
        'dir': './examples/neuralint/',
        'repo': 'brombaut/neuralint',
        'repoversion': '0.0.0'
    }
}
def main():
    args = parser.parse_args()
    exit_if_invalid_args(args)
    docker_files = FileManagement.list_project_docker_files(args.dir)
    repo_dir = os.path.abspath(args.dir)
    repo_name = args.repo
    repo_version = args.repoversion

    docker_image_contents = FileManagement.get_file_contents(docker_files, repo_dir, repo_name, repo_version)
    for file_, json_data in docker_image_contents.items():
        dockerImage = DockerImage()
        dockerImage.analyse(json_data)
        list_instructions = dockerImage.list_instructions
        instructions_options_dict = dockerImage.instructions_options_dict

def exit_if_invalid_args(args):
    if args.testing:
        setattr(args, 'dir', TEST_OPTIONS[args.testing]['dir'])
        setattr(args, 'repo', TEST_OPTIONS[args.testing]['repo'])
        setattr(args, 'repoversion', TEST_OPTIONS[args.testing]['repoversion'])
    if args.dir is None or os.path.isfile(args.dir):
        raise SystemExit("ERROR: -d --dir arg should be directory.")
    if args.repo is None:
        raise SystemExit("ERROR: -r --repo arg should be repo org/name.")
    if args.repoversion is None:
        raise SystemExit("ERROR: -v --repoversion arg should be repo release version.")


if __name__ == "__main__":
    main()