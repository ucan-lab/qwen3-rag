# モデル読み込みや初期化スクリプト
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id="Qwen/Qwen3-1.7B"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype=torch.float16,    # ✅ 精度とメモリ削減
    device_map="auto"             # ✅ GPU/CPU自動対応
)
print(model)
print("✅ Qwen3 モデルとトークナイザーをダウンロードしました。")

# LlamaIndex でのインデックス生成と保存処理
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")

print(embed_model)
print("✅ エンベッドモデルを生成しました。")

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
data_path="./data"
documents = SimpleDirectoryReader(data_path).load_data()
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

print(index)
print("✅ インデックスを生成しました。")

# クエリ実行や対話インタフェース
from llama_index.llms.huggingface import HuggingFaceLLM

llm = HuggingFaceLLM(
    context_window=2048,
    max_new_tokens=512,
    generate_kwargs={"temperature": 0.7},
    tokenizer=tokenizer,
    model=model,
    device_map="auto",
    tokenizer_kwargs={"trust_remote_code": True},
    model_kwargs={"trust_remote_code": True}
)

query_engine = index.as_query_engine(llm=llm, embed_model=embed_model)

print(query_engine)
print("✅ クエリーエンジンを生成しました。")

while True:
    query = input("質問を入力してください（終了するには exit）：")
    if query.lower() in ("exit", "quit"):
        break
    response = query_engine.query(query)
    print('===========回答================')
    print(f"\n回答:\n{str(response)}\n")
