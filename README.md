# Upload Videos to Google Drive


# Monitoramento de Vídeos para Upload no Google Drive

Este projeto é um script em Python que monitora uma pasta específica no seu computador. Sempre que um vídeo é adicionado à pasta monitorada, o script pergunta se você deseja fazer o upload para uma pasta do Google Drive.

## Funcionalidades

- Monitora automaticamente uma pasta local.
- Suporte para formatos de vídeo: `.mp4`, `.mkv`, `.avi`, `.mov`.
- Exibe uma janela de diálogo para confirmação de upload.
- Realiza o upload de vídeos diretamente para uma pasta específica no Google Drive.
- Notificações de sucesso ou erro no envio.
- Registro de atividades no arquivo de log `app.log`.

---

## Requisitos

- Python 3.7 ou superior.
- Credenciais do OAuth 2.0 do Google Drive (`credentials.json`).
- Pacotes Python necessários (instalados via `pip`):
  - `google-auth-oauthlib`
  - `google-auth`
  - `google-api-python-client`
  - `watchdog`
  - `plyer`
  - `tkinter` (incluso em instalações padrão do Python)
- ID da pasta de destino no Google Drive (informe em `UPLOAD_FOLDER_ID`).

---

## Configuração

1. **Obtenha as credenciais do Google Drive**:
   - Acesse o [Google Cloud Console](https://console.cloud.google.com/).
   - Crie um projeto, habilite a API do Google Drive e gere credenciais OAuth 2.0.
   - Baixe o arquivo `credentials.json` e coloque-o na raiz do projeto.

2. **Instale as dependências**:
   ```bash
   pip install google-auth-oauthlib google-auth google-api-python-client watchdog plyer
   ```

3. **Configure o script**:
   - Edite o valor de `FOLDER_TO_WATCH` para apontar para a pasta que você deseja monitorar.
   - Insira o `UPLOAD_FOLDER_ID` da pasta no Google Drive onde os vídeos serão enviados.

---

## Uso

1. Coloque o arquivo `credentials.json` na raiz do projeto.
2. Execute o script:
   ```bash
   python app.py
   ```
3. Adicione vídeos na pasta monitorada. Será exibida uma janela perguntando se deseja fazer o upload.

---

## Estrutura do Projeto

```plaintext
.
├── app.py               # Script principal
├── credentials.json     # Credenciais OAuth 2.0 (obtido no Google Cloud)
├── token.pickle         # Arquivo gerado após autenticação (não editar)
└── app.log              # Arquivo de log das atividades
```

---

## Observações

- Este script utiliza o **OAuth 2.0** para autenticação no Google Drive. Após a autenticação inicial, um token será salvo no arquivo `token.pickle`.
- Certifique-se de que a pasta monitorada seja acessível e que você tenha permissões de gravação no Google Drive.

---

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.
