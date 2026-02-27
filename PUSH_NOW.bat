@echo off
cd /d "%~dp0"
git init
git add .
git config user.name "Syntropy Protocol"
git config user.email "protocol@syntropy.network"
git commit -m "Deployment: Singularidade Sistêmica - Engenharia de Contexto"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/gonpopadma6-sudo/AgenteSYNTROPY.git
git push -u origin main --force
exit /b 0
