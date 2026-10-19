from pinecone_plugin_interface import PluginMetadata
from .assistant import Assistant


try:
    import pinecone
except ImportError as e:
    raise ImportError(
        "This assistant plugin requires the Pinecone SDK to be installed. "
        "Please install the Pinecone SDK by running `pip install pinecone`"
    )

__installables__ = [
    PluginMetadata(
        target_object="Pinecone",
        namespace="assistant",
        implementation_class=Assistant
    ),
]
