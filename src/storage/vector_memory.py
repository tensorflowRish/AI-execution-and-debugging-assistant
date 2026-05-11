import faiss
import numpy as np
import os
import json
from sentence_transformers import SentenceTransformer


class VectorMemory:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = 384

        self.index_file = "src/storage/index.faiss"
        self.meta_file = "src/storage/memory.json"

        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
        else:
            self.index = faiss.IndexFlatIP(self.dimension)

        # load metadata
        if os.path.exists(self.meta_file):
            with open(self.meta_file, "r") as f:
                self.memory = json.load(f)
        else:
            self.memory = []

    def save_disk(self):

        faiss.write_index(self.index, self.index_file)

        with open(self.meta_file, "w") as f:
            json.dump(self.memory, f, indent=4)

    def add_memory(self, error, metadata):

        embedding = self.model.encode([error])

        embedding = np.array(embedding, dtype="float32")

        embedding = np.reshape(embedding, (1, -1))

        faiss.normalize_L2(embedding)

        self.index.add(embedding)

        self.memory.append(metadata)

        self.save_disk()

    def search_memory(self, error, category, k=5):

        if self.index.ntotal == 0:
            return []

        embedding = self.model.encode([error])

        embedding = np.array(
            embedding,
            dtype="float32"
        )

        embedding = np.reshape(
            embedding,
            (1, -1)
        )

        faiss.normalize_L2(embedding)

        distances, indices = self.index.search(
            embedding,
            k
        )

        results = []

        SIMILARITY_THRESHOLD = 0.65

        for score, idx in zip(
            distances[0],
            indices[0]
        ):

            similarity = float(score)

            if similarity >= SIMILARITY_THRESHOLD:

                if 0 <= idx < len(self.memory):

                    item = self.memory[idx]

                    # CATEGORY FILTER
                    if item.get("category") == category:

                        results.append(item)

        return results