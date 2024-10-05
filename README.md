# automate-production-terminal

This README file provides a comprehensive guide on setting up and running the code,including prerequisites, setup instructions, execution, and troubleshooting tips. Once you've created the repository, you can follow these steps to automate your production terminal operations.
—————————————————————————————————————————
To make it easy for users to install all the necessary dependencies, you can add a script to the README that will handle the installation of Python packages and the WebDriver. Below, I’ll include a `setup.sh` script for Unix-based systems (Linux and macOS) and `setup.bat` for Windows users, along with updated instructions in the README.

 Updated README.md with Setup Script

Here’s the updated content for your `README.md` file that includes the setup instructions and script details:

```markdown
 Automate Production Terminal

This project automates accessing a web-based production terminal, selecting the Mob API Terminal, logging into the Ruby on Rails console, and executing Ruby code. This automation is achieved using Python and Selenium.

 Prerequisites

- Python 3.x: Make sure Python is installed on your system.

 Setup

 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/automate-production-terminal.git
cd automate-production-terminal
```

 Step 2: Run the Setup Script

The setup script will install the necessary Python dependencies and download the appropriate WebDriver based on your system.

 For Unix-based Systems (Linux and macOS)

Run the following command to execute the `setup.sh` script:

```bash
bash setup.sh
```

 For Windows Systems

Run the following command to execute the `setup.bat` script:

```cmd
setup.bat
```

The setup script will handle the following:
- Install the Selenium package.
- Download ChromeDriver (for Chrome browser automation) and place it in the current directory.

 Step 3: Update Script Configurations

1. Open `automate_terminal.py`.
2. Replace `your_username`, `your_password`, and `https://your-production-terminal-url.com` with your actual credentials and URL.

 Step 4: Execute the Automation Script

To run the script, use the following command:

```bash
python automate_terminal.py
```

Make sure ChromeDriver is in the same directory as the script, or update the `driver_path` variable with the correct path to ChromeDriver.

 Troubleshooting

- Ensure that ChromeDriver is compatible with your Chrome version. You can check the version of Chrome installed and download the corresponding ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
- Update element locators in the script if the webpage layout changes.

 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or new features.

 License

This project is licensed under the MIT License.
```

 `setup.sh` for Unix-based Systems

Create a file named `setup.sh` in the root directory of your repository and add the following content:

```bash
!/bin/bash

 Install Python dependencies
echo "Installing Python dependencies..."
pip install selenium

 Download ChromeDriver for Unix-based systems
echo "Downloading ChromeDriver..."
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
curl -O "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip"
unzip chromedriver_linux64.zip -d ./
rm chromedriver_linux64.zip

echo "Setup complete!"
```

 `setup.bat` for Windows Systems

Create a file named `setup.bat` in the root directory of your repository and add the following content:

```bat
@echo off

REM Install Python dependencies
echo Installing Python dependencies...
pip install selenium

REM Download ChromeDriver for Windows
echo Downloading ChromeDriver...
curl -O https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_win32.zip
tar -xf chromedriver_win32.zip
del chromedriver_win32.zip

echo Setup complete!
```

These scripts will automatically install Selenium and download ChromeDriver, unzipping it in the directory, so it’s ready for use with your Python script. This should streamline the setup process and make it easier for others to get started.
