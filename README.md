# 🤖 Local RAG Knowledge Base (LlamaIndex + Ollama + Phi-3)

Локальная система поиска и ответов на вопросы по вашей базе знаний (Retrieval-Augmented Generation). Проект работает полностью офлайн на вашем компьютере: без отправки данных в облако, без платных API-ключей и с гарантией конфиденциальности.

---

## 🛠 Технологический стек

* Оркестрация RAG: [LlamaIndex](https://www.llamaindex.ai/)
* Локальная языковая модель (LLM): [Ollama](https://ollama.com/) (phi3)
* Векторные эмбеддинги: HuggingFace (BAAI/bge-small-en-v1.5)
* Среда выполнения: Python 3.8+ (Windows / Linux / macOS)

---

## 📁 Структура проекта

`text
ai_knowledge_base/
│
├── knowledge_base/         # Папка с вашими текстовыми документами
├── script.py               # Основной скрипт запуска RAG
└── README.md               # Документация проекта

www.llamaindex.ai (https://llamaindex.ai/)
LlamaIndex | AI Agents for Document OCR + Workflows
LlamaParse is the world's best agentic OCR for processing complex documents with messy tables, charts, images, and more with human-level accuracy.
