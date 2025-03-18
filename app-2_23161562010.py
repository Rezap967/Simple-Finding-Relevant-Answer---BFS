from collections import deque

def bfs_find_answer(faq_graph, query):
    if query not in faq_graph:
        return "Pertanyaan tidak ditemukan."

    queue, visited = deque([query]), set()

    while queue:
        node = queue.popleft()
        if node in faq_graph.get("answers", {}):
            return faq_graph["answers"][node]

        visited.add(node)
        queue.extend(n for n in faq_graph.get(node, []) if n not in visited)

    return "Jawaban tidak ditemukan."

# Struktur grafik FAQ
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks adalah model AI yang terinspirasi dari otak manusia.",
        "Supervised Learning": "Supervised Learning menggunakan data berlabel untuk pelatihan."
    }
}

# Contoh penggunaan
print("Jawaban:", bfs_find_answer(faq_graph, "What is AI?"))
