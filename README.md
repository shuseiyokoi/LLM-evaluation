# 🤖 LLM Evaluation with Promptfoo — AWS Bedrock Nova Model Comparison

This project demonstrates how to systematically evaluate and compare multiple large language models (LLMs) — specifically **AWS Bedrock's Nova Pro vs. Nova Micro** — using the powerful open-source tool [Promptfoo](https://www.promptfoo.dev/). It provides a reproducible framework for benchmarking model performance within **Retrieval-Augmented Generation (RAG)** systems.

📄 **Blog**: [Promptfoo LLM Evaluation Techniques (Notion)](https://shuseiyokoi.notion.site/Promptfoo-LLM-Evaluation-Techniques-23bf61fbe85c8089ab63e64295bca69c)  
📂 **Repo**: [GitHub](https://github.com/shuseiyokoi/LLM-evaluation/tree/main/aws-model-eval)

<img width="1697" height="1207" alt="Screenshot 2025-07-25 at 15 31 01" src="https://github.com/user-attachments/assets/63ed2eea-935b-43cb-b0e0-79d0cb627bc4" />


---

## 📌 Why This Project?

As the number of LLMs continues to grow — from OpenAI’s GPT-4 to Anthropic’s Claude and AWS’s Nova series — choosing the right model for your business use case becomes challenging.

This project was born out of the need to:
- **Systematically evaluate** models powering my [RAG app](https://main.d1tdd63qxtj4xh.amplifyapp.com/)
- **Compare quality, accuracy, and consistency** of model responses
- **Optimize costs** without sacrificing performance

---

## 🎯 Goals

- Evaluate Nova Pro vs. Nova Micro in real RAG scenarios
- Test performance using automated assertions
- Build a scalable, reproducible, and customizable evaluation pipeline

---

## 🧪 What is Promptfoo?

[Promptfoo](https://www.promptfoo.dev/) is a lightweight framework for:

- Defining **structured test cases** (prompts + expected outcomes)
- Running evaluations across **multiple models**
- Generating **reproducible reports**
- Supporting **custom invocation scripts** (e.g., for AWS Bedrock agents)

---

## 🏗 Architecture

| Component        | Description |
|------------------|-------------|
| Promptfoo        | Evaluation framework |
| AWS Bedrock Nova Pro / Micro | Models under test |
| Custom Python scripts | Model invocation via Bedrock Agent Runtime |
| YAML config      | Defines test cases, assertions, providers |
| HTML report      | Output visualization and sharing |

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/shuseiyokoi/LLM-evaluation.git
cd aws-model-eval
````

### 2. Install dependencies

```bash
npm install -g promptfoo
pip install boto3
```

### 3. Add AWS credentials

Make sure your AWS CLI is configured to access Bedrock agents.

```bash
aws configure
```

### 4. Update Agent IDs

Edit the Python scripts `example_invoke_agent.py`:

```python
AGENT_ID = "your-nova-agent-id"
AGENT_ALIAS_ID = "your-nova-alias-id"
```

---

## 🧪 Running an Evaluation

```bash
promptfoo eval -c model-comparison.yml
```

This will:

* Invoke both Nova Pro and Nova Micro with identical prompts
* Check the responses against structured assertions
* Output side-by-side comparisons and a summary

### ✨ Optional: Generate HTML Report

```bash
promptfoo export --format html --output nova-report.html
open nova-report.html
```

---

## 🧾 Sample Test Case (YAML)

```yaml
description: "Compare Nova Pro vs Nova Micro on career questions"

providers:
  - exec:python3 invoke_bedrock_agent_Nova_Pro.py // I tested two models so there are two invoke function
  - exec:python3 invoke_bedrock_agent_Nova_Micro.py

prompts:
  - "Tell me about Shusei Yokoi's {{topic}}"

tests:
  - description: "Contains background info"
    vars:
      topic: "background"
    assert:
      - type: icontains
        value: "data scientist"
      - type: icontains
        value: "bay area"
```

---

## ✅ Assertion Types Used

| Type           | Use Case                        |
| -------------- | ------------------------------- |
| `icontains`    | Flexible keyword checks         |
| `contains-any` | Multiple possible valid outputs |
| `regex`        | Pattern matching (advanced)     |

---

## 📊 Evaluation Results

| Metric        | Value     |
| ------------- | --------- |
| Duration      | 9 seconds |
| Tests         | 8 passed  |
| Failures      | 0         |
| Errors        | 0         |
| **Pass Rate** | ✅ 100%    |

### 🔍 Observations

* Both Nova Pro and Micro perform excellently for RAG tasks
* Nova Pro gives more **narrative-style** answers
* Nova Micro leans toward **structured bullet/list formats**
* **Micro is more cost-efficient**, yet comparable in performance

---

## 🧠 Advanced Config Patterns

### Run Tests Multiple Times

```yaml
evaluateOptions:
  maxConcurrency: 2
  repeat: 3
```

### Add More Domains

```yaml
- description: "Technical Skills Validation"
  vars:
    topic: "technical expertise in machine learning"
  assert:
    - type: contains-any
      value: ["Python", "R", "SQL", "data analysis"]
```

---

## 📈 Best Practices

1. ✅ Design broad and deep test suites (background, skills, edge cases)
2. 🔍 Mix `icontains`, `contains-any`, and `regex` for robust checking
3. 🤝 Balance automation with human review (style, tone, reasoning)
4. 🔄 Iterate and refine prompts and agents using feedback loops

---

## 🚀 Ideal For

* RAG developers choosing a model backend
* Teams comparing Bedrock, OpenAI, Anthropic, etc.
* AI product managers needing cost-performance insights
* Anyone building **evaluation pipelines** for LLMs

---

## 🔚 Conclusion

This project shows how **Promptfoo + AWS Bedrock** can be used for real-world LLM evaluation at scale. With structured test cases and agent-level customization, you can quickly identify the most effective and cost-efficient model for your application.

📝 **Full Blog**: [Promptfoo LLM Evaluation Techniques](https://shuseiyokoi.notion.site/Promptfoo-LLM-Evaluation-Techniques-23bf61fbe85c8089ab63e64295bca69c)

📂 **GitHub Repo**: [LLM Evaluation](https://github.com/shuseiyokoi/LLM-evaluation/tree/main/aws-model-eval)

---

## 📄 License

MIT License © 2025 [@shuseiyokoi](https://github.com/shuseiyokoi)

---

