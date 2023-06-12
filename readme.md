# Python Automation Projects

Welcome to the Python Automation Projects repository! 🐍✨

Here, you will find a collection of diverse Python automation projects that aim to simplify your life and boost your productivity. Each project showcases the power of automation using Python, demonstrating how we can delegate repetitive tasks to our trusty machines and save valuable time.

## Table of Contents

- [Countdown GUI](#countdown-gui)
- [Website Availbility Checker](#website-availability-checker)
- [Contributing](#contribution-guidelines)


## Countdown GUI

![Countdown GUI](countdown_gui/screenshots/countdown_gui_screenshot.png)

The **Countdown GUI** is an exciting project that provides a glimpse into the world of Python automation. It is a simple graphical user interface created using Python's tkinter GUI toolkit, where you can track the days until a specific event, such as the start of a new semester or an upcoming vacation. This project is designed to inspire you and serve as an excellent starting point for your own automation endeavours.

### Key Features

- Intuitive GUI: Well, I know the universal definition of intuitive, but I'll still assert that the UI is intuitive. The user-friendly interface allows you to easily view the countdown.

- Automation Potential: This project illustrates how Python can automate time-related tasks, providing a practical example of leveraging technology to simplify your schedule.

    A real example of how this could be automated is to set it to launch after every PC startup. For windows:

    - Launch *Run* using `Win+R`
    - In the prompt that opens, type `shell:startup` and click OK
    ![Run Prompt](countdown_gui/screenshots/run_prompt.png)

    - Add the script to the folder that comes up. Now every time your PC starts up, the script will run to display the countdown GUI.
    ![Startup Folder](countdown_gui/screenshots/startup_folder.png)

### Getting Started

To explore the **Countdown GUI** project, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the `countdown_gui` folder.
3. Run the Python script `countdown_gui.pyw` to launch the application.
4. Enjoy the countdown experience and experiment with customisations!

**Disclaimer:** The countdown GUI project is for demonstration purposes only and should not be considered a full-fledged application for critical events or time-sensitive tasks. It is advisable to perform adequate testing and customisation for your specific needs before relying on it for important deadlines or events.

---

## Website Availability Checker

This project is a simple Python script that allows you to check the availability of a website. It sends HTTP requests to the specified URL and determines if the websites are online or experiencing any issues. Additionally, it provides load time information and sends notifications using `plyer`.

### Dependencies

To run the Website Availability Checker, you need to have the following dependencies installed:

- Python 3.x
- requests library
- plyer library

You can install the required dependencies using `pip`. Run the following command:

```python
pip install requests plyer
```

### Usage

1. Clone the repository or download the source code to your local machine.

2. Navigate to the project directory in your command line or terminal.

3. In your command line or terminal, run the following command:

   ```bash
   python website_availability_checker.py
   ```

   The script will start checking the availability of the specified websites every 5 minutes and display the results, including the load time of each website.

4. The script will also send desktop notifications using `plyer` to notify you about the website status. Ensure that you have the necessary permissions set to receive notifications.

### Customisation

You can customise the behaviour of the Website Availability Checker script based on your requirements. Here are some options:

- **Interval**: By default, the script checks the websites every 5 minutes. You can modify this value by locating and modifying this part of the code (time is in milliseconds):

    ```python
    # Schedule the check to run in 5 minutes
    if self.chb_variable_state.get() and result_text[1]:
        self.after(300000, self.check_website_availability)

    ```

- **Notifications**: The script utilizes `plyer` to send desktop notifications. You can customize the notification behaviour by modifying the notification code in the script. For example, you can change the notification message.

- **Error Handling**: The script handles common exceptions and provides basic error handling. You can enhance the error handling logic to address specific scenarios or error types that you encounter.

Please note that the Website Availability Checker is a basic implementation and may not handle all scenarios or account for complex network configurations. It is recommended to enhance and customize the script based on your specific requirements.

---

## Contribution Guidelines

We encourage you to contribute your own automation projects to this repository! Whether it's a small script or a complex application, your creations can inspire and empower others to embrace automation. To contribute, please follow these guidelines:

- Fork this repository and create a new branch for your project.
- Add your project to the appropriate category or create a new one if needed.
- Include a brief description, instructions for usage, and any relevant dependencies.
- Provide clear documentation and comments in your code to aid understanding.
- Submit a pull request, and I'll review your contribution as soon as possible.

Let's automate and simplify our lives together with the power of Python!

Happy coding! 🚀✨

---

Note: This README file serves as a general record for Python automation projects. As the repository grows, you'll find an array of exciting projects covering various aspects of automation. Stay tuned for updates and feel free to explore the existing projects or contribute your own.

For any questions or suggestions, please reach out to me. We're here to support and inspire each other in our automation journeys.

---

