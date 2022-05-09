# Battery Hunter

## How to setup project

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Add your user to the docker group by using a terminal to run: `sudo usermod -aG docker $USER`
3. Sign out and back in again so your changes take effect.
4. Install [Visual Studio Code](https://code.visualstudio.com/)
5. Open vscode and install the extension pack [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
6. In vscode, press CTRL+SHIFT+P, type "open folder in container" and hit enter, select the batteryhunter folder from the file picker.
7. In the vscode built in terminal, verify that you have the ros2 cli available. Hit CTRL+SHIFT+B to build the project. You are now setup and ready for the interview!
