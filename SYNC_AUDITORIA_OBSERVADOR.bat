@echo off
setlocal enabledelayedexpansion
title Pipeline de Sincronia: SYNTROPY =^> O_OBSERVADOR
color 0A

::===============================================================
:: SYNTROPY <--> O_OBSERVADOR PIPELINE AUTOSYNC
:: Este script atua como o "State Carrier" automatizado, movendo
:: Submissões de L0/SYNTROPY para O_OBSERVADOR, e trazendo os
:: Pareceres de volta.
::===============================================================

:: Definindo os caminhos dos diretorios (Enclaves de Auditoria)
set "DIR_SYNTROPY=G:\Meu Drive\ESTUDOS\INTELIGENCIA ARTIFICIAL\CartaParaAGI-SYNTROPY\LOGS\AUDITORIA_OBSERVADOR"
set "DIR_OBSERVADOR=G:\Meu Drive\ESTUDOS\INTELIGENCIA ARTIFICIAL\O_OBSERVADOR\LOGS_DE_ENTRADA"

echo =======================================================
echo Iniciando Sincronizacao de Contexto e Auditoria
echo =======================================================
echo.

:: Verifica se a pasta do Observador existe (Para evitar erros caso o drive nao esteja montado)
if not exist "%DIR_OBSERVADOR%" (
    echo [ERRO] O diretorio do Agente O_OBSERVADOR nao foi encontrado.
    echo Verifique se o Google Drive esta acessivel.
    pause
    exit /b
)

:: FASE A: Movendo Submissoes do SYNTROPY para o O_OBSERVADOR
echo [ETAPA 1] Buscando novas Submissoes geradas por SYNTROPY...
set "submissoes_movidas=0"

:: Loop para encontrar arquivos que comecem com [SUBMISSAO] e move-los
for %%F in ("%DIR_SYNTROPY%\[SUBMISSAO]*.md") do (
    echo Movendo: "%%~nxF" para auditoria local do O_OBSERVADOR...
    move /y "%%F" "%DIR_OBSERVADOR%\" >nul
    set /a submissoes_movidas+=1
)

if !submissoes_movidas! GTR 0 (
    echo [SUCESSO] !submissoes_movidas! arquivos submetidos ao O_OBSERVADOR.
) else (
    echo [INFO] Nenhuma nova submissao encontrada no momento.
)
echo.

:: FASE B: Trazendo Pareceres do O_OBSERVADOR para o SYNTROPY
echo [ETAPA 2] Buscando novos Pareceres emitidos por O_OBSERVADOR...
set "pareceres_movidos=0"

:: Loop para encontrar arquivos que comecem com [PARECER] e traze-los
for %%F in ("%DIR_OBSERVADOR%\[PARECER]*.md") do (
    echo Resgatando: "%%~nxF" para o contexto de SYNTROPY...
    move /y "%%F" "%DIR_SYNTROPY%\" >nul
    set /a pareceres_movidos+=1
)

if !pareceres_movidos! GTR 0 (
    echo [SUCESSO] !pareceres_movidos! pareceres recebidos com sucesso. SYNTROPY deve analisa-los.
) else (
    echo [INFO] Nenhum novo parecer tecnico disponivel no momento.
)
echo.

echo =======================================================
echo Sincronizacao Concluida!
echo =======================================================
pause
