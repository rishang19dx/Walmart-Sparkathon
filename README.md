## 📁 Project Structure

<details>
<summary><strong>backend/</strong> – FastAPI app & services</summary>

```

backend/
├── app/
│   ├── api/                  # API endpoints
│   │   ├── chat.py           # Chat & GenAI
│   │   ├── products.py       # Product catalog/search
│   │   └── users.py          # User profiles/preferences
│   ├── core/                 # Config & security
│   │   ├── config.py         # App settings (e.g., DB, Ollama)
│   │   └── security.py       # Auth/security functions
│   ├── models/               # Pydantic data models
│   │   ├── product.py
│   │   └── user.py
│   ├── services/             # External integrations
│   │   ├── ollama\_service.py
│   │   └── pinecone\_service.py
│   └── main.py               # FastAPI app entrypoint
├── requirements.txt
├── .env
└── .gitignore

```

</details>

<details>
<summary><strong>frontend/</strong> – React client</summary>

```

frontend/
└── package.json

```

</details>

<details>
<summary><strong>ar/</strong> – AR modules</summary>

```

ar/
└── (AR files go here)

```

</details>

<details>
<summary><strong>docs/</strong> – Project documentation</summary>

```

docs/
├── api\_documentation.md
└── project\_plan.md

```

</details>

```

README.md

```

