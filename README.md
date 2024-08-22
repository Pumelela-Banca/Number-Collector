## South African Lottery Number Collector

### Overview
This project is designed to collect and store lottery numbers from the six different lotteries available in South Africa. The collected data is stored in an SQL database for easy access and analysis.

### Features
- **Data Collection**: Automatically fetches the latest lottery numbers from all six South African lotteries using Selenium.
- **Database Storage**: Stores the collected lottery numbers in an SQL table, ensuring data is organized and easily retrievable.
- **Scalability**: Designed to handle large volumes of data efficiently, making it suitable for long-term use.
- **Extensibility**: Easily extendable to include additional features such as data analysis, visualization, and more.

### Technologies Used
- **Python**: The core programming language used for data collection and processing.
- **SQL**: For storing the collected lottery numbers in a structured format.
- **Selenium**: For the web scrapping and number collection.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/south-african-lottery-collector.git
   cd south-african-lottery-collector
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python manage.py migrate
   ```

### Usage
1. Run the data collection script:
   ```bash
   python collect_lottery_numbers.py
   ```
2. Access the stored data through your preferred SQL client or web interface.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License.

