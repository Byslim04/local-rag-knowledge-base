from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# 1. Подключаем бесплатную локальную модель через Ollama
Settings.llm = Ollama(model="phi3", request_timeout=120.0)

# 2. Подключаем бесплатную модель для эмбеддингов
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 3. Загрузка документов из папки knowledge_base
print("⏳ Загружаем документы...")
documents = SimpleDirectoryReader("./knowledge_base").load_data()
print(f"✅ Загружено документов: {len(documents)}")

# 4. Создание индекса
print("⚙️ Создаем векторный индекс...")
index = VectorStoreIndex.from_documents(documents)

# 5. Поисковый движок и запрос
query_engine = index.as_query_engine(similarity_top_k=3)
query = "Как оформить возврат товара?"
print(f"\n🔍 Вопрос: {query}")

response = query_engine.query(query)

print("\n--- Ответ системы ---")
print(response)