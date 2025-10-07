#!/usr/bin/env python3
"""
Script de instalação e configuração do NeoBux
"""

import subprocess
import sys
import os

def instalar_dependencias():
    """Instala as dependências do projeto"""
    print("📦 Instalando dependências...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def criar_banco():
    """Cria o banco de dados"""
    print("🗄️ Criando banco de dados...")
    try:
        from criar_banco import criar_banco
        criar_banco()
        return True
    except Exception as e:
        print(f"❌ Erro ao criar banco de dados: {e}")
        return False

def main():
    """Função principal de instalação"""
    print("🚀 NeoBux - Instalação e Configuração")
    print("=" * 40)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists("requirements.txt"):
        print("❌ Arquivo requirements.txt não encontrado!")
        print("   Certifique-se de estar no diretório correto do projeto.")
        return False
    
    # Instalar dependências
    if not instalar_dependencias():
        return False
    
    # Criar banco de dados
    if not criar_banco():
        return False
    
    print("\n🎉 Instalação concluída com sucesso!")
    print("\n📋 Para executar o projeto:")
    print("   python main.py")
    print("\n🌐 Acesse: http://localhost:5000")
    
    return True

if __name__ == "__main__":
    main()
