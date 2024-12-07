import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import messagebox, Tk
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
from plyer import notification

FOLDER_TO_WATCH = "C:\\Users\\hacke\\Downloads\\testepasta"  # Caminho absoluto da pasta a ser monitorada
SCOPES = ['https://www.googleapis.com/auth/drive.file']
UPLOAD_FOLDER_ID = ""  # ID da pasta do Google Drive


class VideoHandler(FileSystemEventHandler):
    def __init__(self, drive_service):
        self.drive_service = drive_service

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.mp4', '.mkv', '.avi', '.mov')): # Formatos monitorados
            video_path = event.src_path
            video_name = os.path.basename(video_path)
            # Mostrar diálogo para confirmar upload
            root = Tk()
            root.withdraw() 
            root.attributes("-topmost", True)
            upload = messagebox.askyesno("Novo Vídeo Detectado", f"Upload do vídeo '{video_name}' para o Google Drive?", parent=root)
            root.destroy()

            if upload:
                self.upload_to_drive(video_path, video_name)

    def upload_to_drive(self, file_path, file_name):
        file_metadata = {'name': file_name, 'parents': [UPLOAD_FOLDER_ID]}  # Define a pasta de destino
        media = MediaFileUpload(file_path, resumable=True)
        try:
            self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"Upload concluído: {file_name}")
            notification.notify(
                title="Envio Concluído",
                message=f"Arquivo: {file_name}",
                timeout=10
            )
        except Exception as e:
            print(f"Erro ao fazer upload: {e}")
            notification.notify(
                title="Erro no Envio",
                message=f"Erro: {e}",
                timeout=10
            )


def authenticate_drive():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)


def main():
    print("Inicializando monitoramento...")
    drive_service = authenticate_drive()
    event_handler = VideoHandler(drive_service)
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()


import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script iniciado.")
try:
    logging.info("Processando algo...")
except Exception as e:
    logging.error(f"Erro: {e}")
finally:
    logging.info("Script finalizado.")
