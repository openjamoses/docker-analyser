import os
import shutil


class FileManagement:
    @staticmethod
    def list_project_docker_files(directory):
        directory = os.path.abspath(directory)
        list_of_files = list()
        for (dirpath, dirnames, filenames) in os.walk(directory):
            docker_files = list()
            for file in filenames:
                if file.endswith('Dockerfile'):
                    docker_files.append(os.path.join(dirpath, file))
            list_of_files.extend(docker_files)
        return list_of_files

    @staticmethod
    def read_file_source(file):
        try:
            source = open(file, "r")
            return source.read()
        except Exception:
            raise SystemExit("The file doesn't exist or it isn't a Dockerfile ...")

    @staticmethod
    def get_file_contents(files):
        dict_file_contents = {}
        for file in files:
            try:
                source = open(file, "r").read()

                dict_file_contents[file] = source
            except Exception:
                raise SystemExit("The file doesn't exist or it isn't a Dockerfile...")

            #docker_parser = Parser()

            #docker_parser.content = source.read()
            #result.extend(docker_parser.json)
        return dict_file_contents
    @staticmethod
    def remove_clone(repo_root):
        ## Try to remove tree; if failed show an error using try...except on screen
        try:
            shutil.rmtree(repo_root)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))