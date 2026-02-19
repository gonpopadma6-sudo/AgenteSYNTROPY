# 🦅 MANUAL DE DEPLOY - Sincronização Sólida

Este guia garante que a pasta `_GITHUB_SYNC` se torne a versão oficial do seu repositório GitHub, sobrescrevendo qualquer conflito se necessário.

## 📋 Pré-requisitos
1.  Ter o **Git** instalado.
2.  Ter o link do repositório: `https://github.com/gonpopadma6-sudo/AgenteSYNTROPY.git`

## 🚀 Passo a Passo (PowerShell)

Abra o seu terminal (PowerShell) e execute os blocos abaixo, um por um.

### 1. Navegar até a Pasta Segura
```powershell
cd "G:\Meu Drive\ESTUDOS\INTELIGENCIA ARTIFICIAL\AgenteSYNTROPY\_GITHUB_SYNC"
```

### 2. Inicializar ou Reinicializar o Git
Este comando garante que a pasta é um repositório git local.
```powershell
git init
```

### 3. Conectar ao GitHub (Remoto)
Vamos definir o destino. Se já existir, atualizamos a URL.
```powershell
git remote remove origin
git remote add origin https://github.com/gonpopadma6-sudo/AgenteSYNTROPY.git
```
*(Se aparecer erro "No such remote: origin" no primeiro comando, tudo bem, siga para o segundo)*

### 4. Preparar os Arquivos (Stage & Commit)
Adiciona tudo o que está na pasta `_GITHUB_SYNC` para envio.
```powershell
git add .
git commit -m "Deployment: Entropy Optimization Protocols (v2026.1)"
```

### 5. Definir a Branch Principal
Garanta que estamos na branch padrão moderna (`main`).
```powershell
git branch -M main
```

### 6. Enviar para o GitHub (Push Definitivo)
⚠️ O comando abaixo usa `--force` para garantir que o que está no seu PC sobrescreva o que está no GitHub, corrigindo qualquer dessincronização.
```powershell
git push -u origin main --force
```

---

## ✅ Verificação Final
Acesse [https://github.com/gonpopadma6-sudo/AgenteSYNTROPY](https://github.com/gonpopadma6-sudo/AgenteSYNTROPY) e veja se os arquivos técnicos e o `README.md` público estão lá.

**Observação:**
- Se o Git pedir usuário e senha, use suas credenciais do GitHub.
- Se usar autenticação de dois fatores, você pode precisar de um **Personal Access Token** como senha.

## ❓ Solução de Problemas

**Erro: "O termo 'G:\Meu' não é reconhecido..."**
- Isso acontece se você esquecer as aspas ou o comando `cd`.
- **Correto:** `cd "G:\Meu Drive\..."`
- **Errado:** `G:\Meu Drive\...` (sem cd) ou `cd G:\Meu Drive\...` (sem aspas)

**Erro: "fatal: remote origin already exists"**
- Use: `git remote set-url origin https://github.com/gonpopadma6-sudo/AgenteSYNTROPY.git`
