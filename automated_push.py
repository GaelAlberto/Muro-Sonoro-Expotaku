import os
import time
import subprocess

# Configura las variables
repo_path = 'C:/Users/EPEF/Documents/SoundWall/Muro-Sonoro-Expotaku'
watched_folder = 'C:/Users/EPEF/Documents/SoundWall/Muro-Sonoro-Expotaku'
os.chdir(repo_path)

# Función para subir archivos al repositorio
def commit_and_push():
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Automated commit'])
    subprocess.run(['git', 'push'])

# Función para monitorear la carpeta
def monitor_folder():
    last_modified = {}
    while True:
        for file in os.listdir(watched_folder):
            file_path = os.path.join(watched_folder, file)
            if os.path.isfile(file_path):
                modified_time = os.path.getmtime(file_path)
                if file not in last_modified or modified_time > last_modified[file]:
                    print(f'File {file} has been modified. Committing and pushing...')
                    commit_and_push()
                    last_modified[file] = modified_time
        time.sleep(10)  # Espera 10 segundos antes de volver a verificar

if __name__ == "__main__":
    monitor_folder()
