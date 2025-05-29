Absolutely! Let's go over the **types of tools** available in the **OpenAI Agents SDK** and how each one works.

---

## 🧰 Tool Types in OpenAI Agents SDK

There are **three main tool types** you can integrate with an agent:

### 1. 🧠 **Function Calling (Custom Tools)**

These are **functions you define**, and the model can **call them with parameters**.

#### 🔧 Use Case:

Let the agent call an API, calculate something, query a database, etc.

#### ✅ How it works:

1. You define the tool's **name**, **description**, and **parameters schema**.
2. The agent decides when to use the tool and passes the inputs.
3. You receive the call, handle it, return the output.

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]
```

You then provide the result when the agent calls it.

---

### 2. 🧾 **Code Interpreter (a.k.a. Python / Advanced Data Analysis)**

This tool lets the assistant **run Python code**, such as math, plots, or data analysis.

#### 🔧 Use Case:

* Calculate something
* Plot graphs
* Work with CSVs, JSON
* Summarize data

#### ✅ How it works:

* You enable this tool by setting:

  ```python
  tools=[{"type": "code_interpreter"}]
  ```
* The assistant can write and execute code on its own using OpenAI’s built-in Python environment.

---

### 3. 📄 **File Search (via Vector Store)**

Allows the assistant to **search and retrieve information from uploaded documents** using vector embeddings.

#### 🔧 Use Case:

* Chat over PDFs
* Use uploaded files as memory
* FAQ search from docs

#### ✅ How it works:

1. You upload files to a **Vector Store**.
2. Link the store to the assistant:

   ```python
   tool_resources={
       "file_search": {
           "vector_store_ids": [vector_store.id]
       }
   }
   ```
3. The assistant uses the vector store when replying to relevant queries.

---

## 🧩 Combining Tools

You can combine all of them in one assistant:

```python
tools = [
    {"type": "code_interpreter"},
    {"type": "file_search"},
    {
        "type": "function",
        "function": {
            "name": "translate_text",
            "description": "Translate English to French",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    }
]
```

---

## 🌀 How Agent Chooses a Tool

* Based on your query and the assistant’s prompt instructions.
* GPT-4 chooses a tool if it decides one is required to fulfill the request.
* You just handle tool calls when they occur in a run.

---

## ✅ Summary

| Tool Type          | Purpose                            | Setup                 |
| ------------------ | ---------------------------------- | --------------------- |
| `function`         | Call your backend/API/logic        | Define name, params   |
| `code_interpreter` | Run Python for math, CSV, analysis | Just add type         |
| `file_search`      | Search through documents           | Upload + vector store |

---

Would you like a hands-on example of one of these (e.g., code interpreter, file search, or a function tool)?
