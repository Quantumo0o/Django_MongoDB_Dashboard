# 🌟 Data Visualization Dashboard 🌟

Welcome to the Data Visualization Dashboard! This project is designed to help you explore and visualize data interactively, using the powerful combination of Django, MongoDB, and Google Charts. Dive into your data and uncover insights with ease!

## 🚀 Features

- **Interactive Visualizations**: Dynamic charts and maps powered by Plotly.js.
- **Comprehensive Filters**: Easily filter data by year, topic, sector, region, and more.
- **Real-time Data Fetching**: Seamless data retrieval from MongoDB.

## 🛠️ Setup and Installation

### Prerequisites

Before you begin, ensure you have the following:

- Python 3.x
- MongoDB

### Installation

Follow these steps to get the project up and running:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/data-visualization-dashboard.git
    cd data-visualization-dashboard
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    Create a `.env` file in the project root and add your MongoDB connection string:

    ```
    DATABASE_URL=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
    ```

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Explore the Dashboard**:

    Open your browser and go to `http://127.0.0.1:8000` to start exploring!

## 📊 Usage

- The dashboard showcases various visualizations of your data.
- Utilize the filters on the left to refine the data displayed.


## 🧰 Dependencies

- Django==3.2
- djongo==1.3.6
- djangorestframework==3.14.0
- django-environ==0.11.2
- django-filter==23.5
- dnspython==2.6.1
- python-dotenv==1.0.1
- setuptools==65.5.0

## 🤝 Contributing

We welcome contributions! Feel free to submit a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy visualizing! 🌟


