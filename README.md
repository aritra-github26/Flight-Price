# Flight Price Prediction

This project aims to predict flight prices using machine learning techniques. By analyzing historical flight data, we can build a model that can accurately estimate the price of a flight based on various factors such as departure time, airline, route, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. Clone the repository: `git clone https://github.com/aritra-github26/Flight-Price.git`
2. Navigate to the project directory: `cd Flight-Price`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

To use the flight price prediction model, follow these steps:

1. The model can be trained by using this command: `python src/pipelines/training_pipeline.py`
2. Run the web-app using this command: `python app.py`
3. Provide the necessary inputs to the model through the web-app, such as departure time, airline, source, destination, etc.
4. Get the predicted flight price as the output.

## Data

The flight data used for this project is sourced from various airlines and travel agencies. It includes information such as departure time, arrival time, airline, route, and price. The dataset is preprocessed and cleaned to remove any inconsistencies or missing values.

## Model Training

The flight price prediction model is trained using a machine learning algorithm called Extreme Gradient Boosting Regression (with hyperparameter tuning by Grid Search Cross Validation). This algorithm is chosen for its ability to handle both numerical and categorical features effectively. The model is trained on a labeled dataset, where the flight prices are the target variable.

## Evaluation

The performance of the flight price prediction model is evaluated using various metrics R-squared score. These metrics help assess the accuracy and reliability of the model's predictions.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Make sure to follow the project's code of conduct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
