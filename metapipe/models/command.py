""" A command model that can be easily transformed into jobs.

author: Brian Schrader
since: 2015-12-21
"""

from .tokens import Input, Output, FileToken, PathToken


class Command(object):

    def __init__(self, alias, parts=[], dependencies=[]):
        self.alias = alias
        self.parts = parts
        self.dependencies = dependencies
        for output in self.output_parts:
            output.alias = self.alias
        
    def __repr__(self):
        return '<Command: {}>'.format(self.alias)
        
    def update_dependent_files(self, prev_commands=[]):
        """ Update the command's dependencies based on the evaluated input and 
        output of previous commands. 
        """
        for command in prev_commands:
            for part in self.parts:
                for other_file in command.output_parts:
                    if (part in self.input_parts 
                        and other_file == part):
                        part.filename = other_file.eval()
                                
    def eval(self):
        """ Evaluate the given job and return a complete shell script to be run
        by the job manager.
        """
        eval = []
        for part in self.parts:
            try:
                result = part.eval()
            except AttributeError:
                result = part
            eval.append(result)
        return ' '.join(eval)

    @property
    def input_parts(self):
        """ Returns a list of the input tokens in the list of parts. """
        return [part for part in self.file_parts
            if isinstance(part, Input)]
        
    @property
    def output_parts(self):
        """ Returns a list of the output tokens in the list of parts. """
        return [part for part in self.file_parts
            if isinstance(part, Output)]

    @property
    def file_parts(self):
        """ Returns a list of the file tokens in the list of parts. """
        file_parts = []
        for part in self.parts:
            try:
                for sub_part in part:
                    if isinstance(sub_part, FileToken):
                        file_parts.append(sub_part)
            except TypeError:
                if isinstance(part, FileToken):
                    file_parts.append(part)
        return file_parts
        
    @property
    def path_parts(self):
        """ Returns a list of the path tokens in the list of parts. """
        return [part for part in self.parts
            if isinstance(part, PathToken)]
