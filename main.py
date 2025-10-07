from NeoStore import app

if __name__ == "__main__":
    print("🚀 Iniciando servidor NeoBux...")
    print("📱 Acesse: http://localhost:5000")
    print("🛑 Para parar o servidor, pressione Ctrl+C")
    app.run(debug=True, host='0.0.0.0', port=5000)