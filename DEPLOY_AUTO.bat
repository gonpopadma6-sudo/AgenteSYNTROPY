@echo off
echo ========================================================
echo   INICIANDO DEPLOY AUTOMATICO - AGENTE SYNTROPY
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/5] Inicializando repositorio...
git init

echo [2/5] Adicionando arquivos...
git add .

echo [2.5/5] Configurando identidade local (Camuflagem)...
git config user.name "Syntropy Protocol"
git config user.email "protocol@syntropy.network"

echo [3/5] Criando commit de camuflagem...
git commit -m "Deployment: Entropy Optimization Protocols (v2026.1)"

echo [4/5] Configurando repositorio remoto...
git branch -M main
git remote remove origin
git remote add origin https://github.com/gonpopadma6-sudo/AgenteSYNTROPY.git

echo [5/5] Enviando para o GitHub (Forcando atualizacao)...
git push -u origin main --force

echo.
echo ========================================================
echo   PROCESSO FINALIZADO
echo ========================================================
echo Verifique se nao houve erros de autenticacao acima.
pause
