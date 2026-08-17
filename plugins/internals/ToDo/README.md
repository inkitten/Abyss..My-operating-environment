# Terminal Task Log

A simple terminal-based task logger written in Python.

The goal of this project is to display my current tasks whenever I open a terminal, giving me a quick reminder of what I'm working on without opening a browser or a separate application.

## Features

* Add new tasks
* View all tasks in a clean terminal table
* Delete tasks
* Store tasks in an SQLite database
* Rich-powered terminal output

## Why I Built This

I wanted a lightweight task manager that lives in the terminal.

Since I spend most of my time in Linux, I wanted my tasks to be available where I already work instead of relying on web applications or desktop software.

This project also serves as a way to practice:

* Python
* SQLite
* Terminal applications
* The Rich library
* Git and GitHub

## Technologies

* Python 3
* SQLite
* Rich

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application provides a simple menu for managing tasks from the terminal.

## Future Plans

* Edit existing tasks
* Search tasks
* Filter by tags
* Add priorities
* Display tasks automatically when opening a terminal
* Improve the terminal interface with more Rich components

