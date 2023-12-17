from langchain.text_splitter import (
    TextSplitter,
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)

from ix.api.components.types import NodeTypeField
from ix.chains.fixture_src.parsers import LANGUAGE
from ix.chains.fixture_src.targets import DOCUMENT_LOADER_TARGET


CHARACTER_SPLITTER_CLASS_PATH = "langchain.text_splitter.CharacterTextSplitter"
CHARACTER_SPLITTER = {
    "class_path": CHARACTER_SPLITTER_CLASS_PATH,
    "type": "text_splitter",
    "name": "CharacterTextSplitter",
    "description": CharacterTextSplitter.__doc__,
    "fields": NodeTypeField.get_fields(
        TextSplitter.__init__,
        include=[
            "separator",
            "chunk_size",
            "chunk_overlap",
            "keep_separator",
            "add_start_index",
        ],
    ),
}


RECURSIVE_CHARACTER_SPLITTER_CLASS_PATH = (
    "langchain.text_splitter.RecursiveCharacterTextSplitter.from_language"
)

RECURSIVE_CHARACTER_SPLITTER = {
    "class_path": RECURSIVE_CHARACTER_SPLITTER_CLASS_PATH,
    "type": "text_splitter",
    "name": "RecursiveCharacterTextSplitter",
    "description": RecursiveCharacterTextSplitter.__doc__,
    "fields": [LANGUAGE]
    + NodeTypeField.get_fields(
        TextSplitter.__init__,
        include=[
            "chunk_size",
            "chunk_overlap",
            "keep_separator",
            "add_start_index",
        ],
    ),
    "connectors": [DOCUMENT_LOADER_TARGET],
}

TEXT_SPLITTERS = [RECURSIVE_CHARACTER_SPLITTER, CHARACTER_SPLITTER]

__all__ = ["TEXT_SPLITTERS", "RECURSIVE_CHARACTER_SPLITTER_CLASS_PATH"]
