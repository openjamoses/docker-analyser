from analysis.DockerOptions import ImageOptions
class DockerImage:
    def __init__(self):
        self.imageOptions = ImageOptions()
        self.list_instructions = []
        self.instructions_options_dict = {}
    def analyse(self, json_data):
        for row in json_data:
            self.list_instructions.extend([key for key in row.keys() if key != 'COMMENT'])
            for key, val in row.items():
                if key != 'COMMENT':
                    for key2, val2 in self.imageOptions.options_dict.items():
                        for i in val2:
                            for v_split in str(val).split():
                                if i == v_split:
                                    if i in self.instructions_options_dict.keys():
                                        self.instructions_options_dict[i] += 1
                                    else:
                                        self.instructions_options_dict[i] = 1
