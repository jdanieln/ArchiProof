import subprocess
import sys

def run_command(command):
    print(f"👉 Ejecutando: {command}")
    try:
        subprocess.check_call(command, shell=True)
        print("✅ Hecho.")
    except subprocess.CalledProcessError:
        print("❌ Error ejecutando el comando.")
        sys.exit(1)

def main():
    print("🚀 Iniciando configuración robusta del entorno ArchiProof...")

    # Paso 1: Actualizar herramientas de instalación (clave para evitar el error de grpcio)
    run_command(f"{sys.executable} -m pip install --upgrade pip setuptools wheel")

    # Paso 2: Instalar grpcio forzando binarios (el truco mágico)
    run_command(f"{sys.executable} -m pip install grpcio --only-binary=:all:")

    # Paso 3: Instalar el resto de dependencias
    run_command(f"{sys.executable} -m pip install -r requirements.txt")

    print("\n🎉 ¡Entorno configurado correctamente! Ya puedes ejecutar 'python main.py'")

if __name__ == "__main__":
    main()