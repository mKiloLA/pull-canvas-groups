# pull-canvas-groups

## Installation Steps

1. Install Python 3.11 from [Python's website](https://www.python.org/downloads/release/python-3116/).
2. Clone this repository to your favorite repo location.
3. Open up PowerShell and navigate to the project root directory.
4. In the command line, type:

    ```bash
    pip install -r requirements.txt
    ```

5. After requirements are installed, run the following command in the command line:

    ```bash
    pyinstaller src/__main__.py --name CanvasGroupData --noconfirm --onefile --noconsole
    ```

    If Windows Defender prevents this command from running, try removing the `--noconsole` command line option.

6. Once the installation has completed, create a new file named `config.toml` in the `dist` folder. See [example_config.toml](example_config.toml) for an example of the format.

    * Replace the text `API Token` with your own API token. For instructions on generating an API token, see this [article](https://kb.iu.edu/d/aaja#:~:text=Log%20into%20Canvas%20and%2C%20on,fill%20out%20all%20required%20information.) from Indiana Univeristy.

7. At this point, the set up is complete and the program is ready to be used. Open the `dist` folder in File Explorer and run the executable and the following GUI will appear:

    <p align="center">
    <img src="images\GUI.png" alt="GUI Image"/>
    </p>

8. To get the class number, open Canvas and navigate to the course you need Group Data for and look at the URL. The number at the end of the URL is the class number.

    <p align="center">
    <img src="images\CanvasURL.png" alt="URL Image"/>
    </p>

9. Enter the number into the text box and hit submit. After a moment of waiting, the .xlsx file with the name of the course will be saved to your downloads folder.

    <p align="center">
    <img src="images\ExampleExcel.png" alt="Example Excel Output"/>
    </p>

    The program can run multiple times in a row, but the labels do not reset.
