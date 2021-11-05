from dockerfile_parse import DockerfileParser
import json

class ImageParser:
    def __init__(self, src):
        self.src = src
    def parse(self):
        dfp = DockerfileParser()