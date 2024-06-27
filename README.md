Here is the updated README with the specified Python version and package dependencies:

---

# 🌟 Data Visualization Dashboard 🌟

Welcome to the Data Visualization Dashboard! This innovative project is crafted to empower users with interactive and insightful visualizations, seamlessly blending the power of Django, MongoDB, and Google Charts. Whether you're a data enthusiast, analyst, or developer, this dashboard is your gateway to uncovering hidden insights and making data-driven decisions with ease.

## 🌐 Why Data Visualization Dashboard?

In today's data-driven world, understanding and interpreting data is crucial. The Data Visualization Dashboard offers:

- **📊 Interactive Visualizations**: Bring your data to life with dynamic charts and maps.
- **🖥️ User-Friendly Interface**: Intuitive design ensures a smooth user experience.
- **🔍 Comprehensive Filters**: Tailor your data exploration with easy-to-use filters.
- **⏱️ Real-Time Data Updates**: Stay up-to-date with the latest data pulled directly from MongoDB.

## 🚀 Key Features

- **📈 Dynamic Charts and Maps**: Utilize Google Charts to create interactive bar charts, pie charts, choropleth maps, and more.
- **🔧 Filter and Explore**: Easily filter data by year, topic, sector, region, and other categories.
- **⚙️ Customizable Dashboards**: Modify and extend the dashboard to fit your unique data needs.
- **🔗 Backend-Frontend Integration**: Smooth communication between Django backend and frontend, ensuring a seamless data experience.

## 🌟 Who is it for?

- **📊 Data Analysts**: Explore and visualize data trends effortlessly.
- **👩‍💻 Developers**: Integrate and extend the dashboard for custom projects.
- **💼 Business Professionals**: Make informed decisions with clear data insights.
- **🎓 Educators and Students**: Teach and learn data visualization techniques.

## 📦 How to Use This Project

### Prerequisites

- 🐍 Python 3.10.11
- 🍃 MongoDB

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/data-visualization-dashboard.git
   cd data-visualization-dashboard
   ```

2. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the project root directory and add the following variables:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=mongodb://your_mongodb_uri
   ```

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Load Initial Data**

   ```bash
   python manage.py loaddata initial_data.json
   ```

### Running the Project

1. **Start the Django Development Server**

   ```bash
   python manage.py runserver
   ```

2. **Access the Dashboard**

   Open your web browser and navigate to `http://localhost:8000/dashboard/`.

### Project Structure

- **Backend**: Django framework to manage data and APIs.
- **Frontend**: HTML, CSS, JavaScript (jQuery, Google Charts) for the dashboard interface and visualizations.
- **Database**: MongoDB for storing and managing the data.

### Customization

Feel free to customize the dashboard as per your needs. You can:

- Add new filters.
- Modify existing visualizations.
- Integrate additional data sources.
- Enhance the UI/UX with new styles and components.

### 🤝 Contributing

We welcome contributions! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request.


## 📜 License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

---

Happy visualizing! 🌟


