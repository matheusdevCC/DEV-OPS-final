# 🚀 Projeto Final DevOps – Pipeline CI/CD + Testes + Deploy em Produção

Bem-vindo ao repositório do **Projeto Final de DevOps**!  
Aqui você encontrará uma aplicação Python com API Flask totalmente integrada a uma Pipeline CI/CD no **GitHub Actions**, testes automatizados e validação do ambiente de produção no **Render**.

---

## 📌 Objetivo do Projeto
Construir uma pipeline DevOps completa e robusta que realiza:

- ✔ **Análise de qualidade de código (flake8)**  
- ✔ **Build automatizado**  
- ✔ **Execução de testes unitários**  
- ✔ **Smoke tests direto no ambiente de produção**  
- ✔ **Deploy real via Render**  
- ✔ **Fluxo CI/CD completo com 3 jobs profissionais**

Este projeto representa a aplicação prática de conceitos de automação, testes, versionamento, cloud e cultura DevOps.

---

## 🌐 Aplicação Online (Render)

👉 **https://dev-ops-final.onrender.com**

### Endpoints da API:

| Método | Rota        | Descrição |
|-------|-------------|-----------|
| GET   | `/`         | Verifica se a API está online |
| GET   | `/items`    | Lista itens mockados |
| POST  | `/login`    | Gera token JWT fake |
| GET   | `/protected`| Rota protegida (exige token) |

---

## 🧪 Testes Unitários

O arquivo **test_app.py** inclui:

- ✔ Teste do endpoint `/`
- ✔ Teste de obtenção de token `/login`
- ✔ Teste de acesso proibido em `/protected`

Os testes são executados automaticamente pela pipeline.

---

## 🔧 Estrutura do Projeto

📂 DEV-OPS-final
├── application.py # API principal
├── requirements.txt # Dependências da aplicação
├── test_app.py # Testes unitários
├── README.md # Documentação
└── .github/
└── workflows/
└── ci.yml # Pipeline CI/CD completa


---

## ⚙️ Pipeline CI/CD (GitHub Actions)

A pipeline possui **3 jobs**, organizados profissionalmente:

### 1️⃣ quality_check  
✔ Executa flake8 para verificar estilo e erros superficiais.

### 2️⃣ build_and_test  
✔ Instala dependências  
✔ Roda testes unitários  
✔ Garante integridade antes de liberar build

### 3️⃣ deploy_stage  
✔ NÃO faz deploy (o Render já cuida disso)  
✔ Executa *smoke tests reais* em produção:

- `/`
- `/items`
- `/login`






