# Indoor Localization of Target Node

## Project Overview

This project compares two methods for **indoor localization** of a target node: **Triangulation** (using 3 Access Points) and **Square Method** (using 4 Access Points). By leveraging **regression models**, we aim to determine which method provides more accurate localization results in different environments.

## Problem Statement

**Indoor localization** is vital for location-based services in environments where GPS is ineffective. This project focuses on localizing a target node inside buildings using two distinct approaches: Triangulation and Square Method, to determine which is more efficient and accurate under varying conditions.

## Tools and Technologies

- **Programming Languages**: Python
- **Libraries**:
  - **Data Science & Machine Learning**: Numpy, Pandas, Scikit-learn
  - **Algorithms**: Regression Models, Triangulation, Square Localization Methods
- **Data**: Indoor datasets from IIT Jammu with varying conditions (obstacles and open spaces)

## Approach

1. **Triangulation (3 APs)**: Localizes the target node using signals from three access points.
2. **Square Method (4 APs)**: Localizes the target node using signals from four access points.
  
### Experimentation:
- **Room 1**: (Nescafe area, IIT Jammu) - Contains obstacles with 17 datasets.
  - **Outcome**: Triangulation produced better results with higher accuracy and lower error metrics (MSE, MAE).
  
- **Room 2**: (Open space, IIT Jammu) - 1.5k+ datasets without obstacles.
  - **Outcome**: Square Method showed higher error rates and lower accuracy.

## Results

- **Triangulation** method consistently outperformed **Square Method**, achieving better accuracy and lower error metrics in both obstructed and open environments.
- Triangulation was especially effective in the presence of obstacles, while the Square method showed limitations in open spaces.

## Conclusion

- **Triangulation** is the more reliable method for indoor localization.
- **Square Method** is less accurate and is recommended only in certain conditions where environmental factors are ideal.

## Setup and Installation

To run the code and experiment with the datasets:

### Prerequisites
Ensure Python 3.x is installed. You will need the following libraries:

```bash
numpy
pandas
scikit-learn


