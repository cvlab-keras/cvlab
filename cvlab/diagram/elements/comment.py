from .base import *


class TextComment(NormalElement):
    name = 'Comment'
    comment = 'Element containing text editor'

    def get_attributes(self):
        return [], [], [CommentParameter(id="editor", value="")]


register_elements_auto(__name__, locals(), "Others", 30)
