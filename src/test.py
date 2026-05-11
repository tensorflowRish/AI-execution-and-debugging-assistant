from storage.vector_memory import VectorMemory

vm = VectorMemory()

vm.add_memory(
    "ModuleNotFoundError: dotenv",
    {"fix": "pip install python-dotenv"}
)

print(vm.search_memory("No module named dotenv"))