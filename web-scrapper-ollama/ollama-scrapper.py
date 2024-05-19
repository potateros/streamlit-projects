import streamlit as st
from scrapegraphai.graphs import SmartScraperGraph

st.title("Ollama Scrapper")

graph_config = {
  "llm": {
    "model": "ollama/llama3",
    "temperature": 0,
    "format": "json",
    "base_url": "http://localhost:11434",
  },
  "embeddings": {
    "model": "ollama/nomic-embed-text",
    "base_url": "http://localhost:11434",
  },
  "verbose": True
}

url = st.text_input("Enter URL:")
prompt = st.text_input("What do you want to scrape?")

scrapper_graph = SmartScraperGraph(
  prompt=prompt,
  source=url,
  config=graph_config
)

if st.button("Start"):
  result = scrapper_graph.run()
  st.write(result)
