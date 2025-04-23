# Whiteboard Application

This is a simple whiteboard application that allows users to draw various shapes on a digital canvas. The application provides an intuitive interface for creating and managing drawings.

## Project Structure

```
whiteboard-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── utils
│   │   └── helpers.py   # Utility functions for input validation and calculations
│   ├── models
│   │   └── shapes.py    # Classes representing different drawable shapes
│   └── services
│       └── drawing_service.py  # Manages drawing operations on the whiteboard
├── requirements.txt      # Lists dependencies for the project
├── .gitignore            # Specifies files to ignore in version control
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd whiteboard-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Follow the on-screen instructions to interact with the whiteboard. You can draw shapes, clear the board, and save your work.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.